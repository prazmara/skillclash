#!/usr/bin/env python
"""Analysis for ClashBench runs. Usage: python analyze.py <model_tag>

Reads runs/<tag>/diag.jsonl, treat*.jsonl (all files are merged; treat_v1.jsonl is a legacy file and is skipped),
ablate.jsonl, variance.jsonl and compile_trace.json when they exist. Writes runs/<tag>/analysis.json and prints tables.

Unit of inference is the job (a skill pair). Every interval is a 95% percentile bootstrap over jobs
(10,000 resamples, seed 0). The main analysis uses all planted rules. The "valid" sensitivity analysis keeps
rules that the model follows at least half the time with the skill alone and at most half the time with no skill.
"""
import collections
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from spec import target_set  # noqa: E402
import jobs_core  # noqa: E402
import jobs_extra  # noqa: E402

JOBS = list(jobs_core.JOBS) + list(jobs_extra.JOBS)
tag = sys.argv[1]
RNG = np.random.default_rng(0)


def load(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


def boot(vals):
    v = np.array([x for x in vals if x is not None and not np.isnan(x)], float)
    if len(v) == 0:
        return dict(mean=None, lo=None, hi=None, n=0)
    m = v[np.random.default_rng(0).integers(0, len(v), (10000, len(v)))].mean(1)
    return dict(mean=float(v.mean()), lo=float(np.percentile(m, 2.5)), hi=float(np.percentile(m, 97.5)), n=int(len(v)))


def fmt(b):
    return "n/a" if b["mean"] is None else f"{100 * b['mean']:5.1f} [{100 * b['lo']:5.1f}, {100 * b['hi']:5.1f}]"


def excl(s, L):
    return float(np.mean([s[f"{L}.e{i}"] for i in (1, 2, 3)]))


def takeover(s):
    a, b = excl(s, "A"), excl(s, "B")
    return float((a >= 0.99 and b <= 0.01) or (b >= 0.99 and a <= 0.01))


def both_full(s):
    return float(excl(s, "A") >= 0.99 and excl(s, "B") >= 0.99)


def over_jobs(per_job):
    return boot([float(np.mean(v)) for v in per_job.values() if len(v)])


diag = load(f"{ROOT}/runs/{tag}/diag.jsonl")
D = collections.defaultdict(list)
for r in diag:
    D[(r["job"], r["cond"])].append(r["scores"])
jobs = [j for j in JOBS if (j.id, "A") in D]
out = dict(model=tag, n_jobs=len(jobs), n_diag=len(diag))
if not jobs:
    sys.exit(f"no diagnosis records for {tag}")


def rate(job, cond, key):
    s = D.get((job, cond), [])
    return float(np.mean([x[key] for x in s])) if s else None


# ---- rule validity (sensitivity analysis)
valid, tab = {}, collections.Counter()
for j in jobs:
    for L in "AB":
        for r in j.skills[L].reqs:
            k = f"{L}.{r.key}"
            valid[(j.id, k)] = rate(j.id, L, k) >= 0.5 and rate(j.id, "none", k) <= 0.5
            tab[(r.rel, valid[(j.id, k)])] += 1
out["valid_rules"] = {rel: dict(valid=tab[(rel, True)], total=tab[(rel, True)] + tab[(rel, False)]) for rel in ("excl", "sh", "ent", "con")}
print(f"model {tag}: {len(jobs)} jobs, {len(diag)} diagnosis records")
print("rules valid / total by relation:", out["valid_rules"])


def keys(j, L, rels, only_valid):
    return [f"{L}.{r.key}" for r in j.skills[L].reqs if r.rel in rels and (not only_valid or valid[(j.id, f'{L}.{r.key}')])]


def mean_rate(j, conds, ks):
    v = [rate(j.id, c, k) for c in conds for k in ks]
    v = [x for x in v if x is not None]
    return float(np.mean(v)) if v else None


# ---- TABLE 1: own-rule fidelity alone, with an unrelated skill, with the clashing skill
res = {}
GROUPS = (("all own rules", ("excl", "sh", "ent", "con")), ("satisfiable", ("excl", "sh", "ent")), ("exclusive", ("excl",)), ("shared", ("sh",)),
          ("entangled", ("ent",)), ("contradictory", ("con",)))
for only_valid in (False, True):
    t = {}
    for name, rels in GROUPS:
        ag = {}
        for j in jobs:
            rows = []
            for L in "AB":
                ks = keys(j, L, rels, only_valid)
                if ks:
                    rows.append((mean_rate(j, ["none"], ks), mean_rate(j, [L], ks), mean_rate(j, [L + "C", "C" + L], ks), mean_rate(j, ["AB", "BA"], ks)))
            if rows:
                ag[j.id] = np.mean(np.array(rows, float), 0)
        if not ag:
            continue
        a = np.array(list(ag.values()))
        t[name] = dict(no_skill=boot(a[:, 0]), alone=boot(a[:, 1]), with_unrelated=boot(a[:, 2]), with_clashing=boot(a[:, 3]),
                       delta_unrelated=boot(a[:, 2] - a[:, 1]), delta_clashing=boot(a[:, 3] - a[:, 1]))
    res["valid" if only_valid else "all"] = t
    print(f"\n=== TABLE 1 ({'valid rules only' if only_valid else 'all rules'}): share of a skill's own rules satisfied (%), mean over jobs [95% CI]")
    print(f"{'rule group':15s} {'no skill':>20s} {'skill alone':>20s} {'+ unrelated skill':>20s} {'+ clashing skill':>20s} {'change':>22s}")
    for name, v in t.items():
        print(f"{name:15s} {fmt(v['no_skill']):>20s} {fmt(v['alone']):>20s} {fmt(v['with_unrelated']):>20s} {fmt(v['with_clashing']):>20s} {fmt(v['delta_clashing']):>22s}")
out["diagnosis"] = res

# ---- takeover, contradiction winner, entangled pair
tk, bf, cw, ej, es = (collections.defaultdict(list) for _ in range(5))
for j in jobs:
    c = collections.Counter()
    for cond in ("AB", "BA"):
        first, second = cond[0], cond[1]
        for s in D[(j.id, cond)]:
            tk[j.id].append(takeover(s))
            bf[j.id].append(both_full(s))
            ej[j.id].append(float(s["A.ent"] and s["B.ent"]))
            a, b = s[f"{first}.con"], s[f"{second}.con"]
            c["first" if a and not b else "second" if b and not a else "neither" if not a and not b else "both"] += 1
    n = sum(c.values())
    for k in ("first", "second", "neither"):
        cw[k].append(c[k] / n)
    es[j.id].append(rate(j.id, "A", "A.ent") * rate(j.id, "B", "B.ent"))
out["takeover"] = dict(one_skill_fully_other_not_at_all=over_jobs(tk), both_fully=over_jobs(bf),
                       corr_exclA_exclB=float(np.corrcoef([excl(s, "A") for j in jobs for c in ("AB", "BA") for s in D[(j.id, c)]],
                                                          [excl(s, "B") for j in jobs for c in ("AB", "BA") for s in D[(j.id, c)]])[0, 1]))
out["contradiction"] = dict(first_listed_wins=boot(cw["first"]), second_listed_wins=boot(cw["second"]), neither=boot(cw["neither"]))
out["entangled_joint"] = dict(both_loaded=over_jobs(ej), product_of_singles=over_jobs(es))
out["takeover_per_job"] = {j.id: float(np.mean(tk[j.id])) for j in jobs}
out["both_fully_per_job"] = {j.id: float(np.mean(bf[j.id])) for j in jobs}
Dt = {(r["job"], r["cond"], r["task"]): r["scores"] for r in diag}


def win(s):
    a, b = excl(s, "A"), excl(s, "B")
    return "A" if a >= 0.99 and b <= 0.01 else "B" if b >= 0.99 and a <= 0.01 else "mixed"


same, firstboth, secondboth, firstshare = (collections.defaultdict(list) for _ in range(4))
n_both_orders = 0
for j in jobs:
    for t in range(len(j.tasks)):
        if (j.id, "AB", t) not in Dt or (j.id, "BA", t) not in Dt:
            continue
        wab, wba = win(Dt[(j.id, "AB", t)]), win(Dt[(j.id, "BA", t)])
        for cond, w in (("AB", wab), ("BA", wba)):
            if w != "mixed":
                firstshare[j.id].append(float(w == cond[0]))
        if wab != "mixed" and wba != "mixed":
            n_both_orders += 1
            same[j.id].append(float(wab == wba))
            firstboth[j.id].append(float(wab == "A" and wba == "B"))
            secondboth[j.id].append(float(wab == "B" and wba == "A"))
def pooled(dd):
    v = [x for vv in dd.values() for x in vv]
    return float(np.mean(v)) if v else None


def takeover_valid(j, s):
    ka = [f"A.e{i}" for i in (1, 2, 3) if valid[(j.id, f"A.e{i}")]]
    kb = [f"B.e{i}" for i in (1, 2, 3) if valid[(j.id, f"B.e{i}")]]
    if not ka or not kb:
        return None
    a, b = np.mean([s[k] for k in ka]), np.mean([s[k] for k in kb])
    return float((a >= 0.99 and b <= 0.01) or (b >= 0.99 and a <= 0.01))


tkval = collections.defaultdict(list)
for j in jobs:
    for cond in ("AB", "BA"):
        for s in D[(j.id, cond)]:
            v = takeover_valid(j, s)
            if v is not None:
                tkval[j.id].append(v)
out["takeover"]["valid_exclusive_rules_only"] = over_jobs(tkval)
out["order"] = dict(requests_with_takeover_in_both_orders=n_both_orders, same_skill_wins_both_orders=over_jobs(same),
                    pooled_same_skill_wins_both_orders=pooled(same), pooled_first_listed_share_of_takeovers=pooled(firstshare),
                    n_jobs_same=sum(1 for v in same.values() if v), n_jobs_firstshare=sum(1 for v in firstshare.values() if v),
                    n_takeovers=sum(len(v) for v in firstshare.values()),
                    first_listed_wins_both_orders=over_jobs(firstboth), second_listed_wins_both_orders=over_jobs(secondboth),
                    first_listed_share_of_takeovers=over_jobs(firstshare))
print("\n=== TAKEOVER when both skills are loaded (exclusive rules; % of outputs)")
print(f"  one skill fully, the other not at all  {fmt(out['takeover']['one_skill_fully_other_not_at_all'])}")
print(f"  both skills fully                      {fmt(out['takeover']['both_fully'])}")
print(f"  correlation of the two skills' exclusive-rule compliance: {out['takeover']['corr_exclA_exclB']:+.2f}")
print(f"  contradiction: first-listed wins {fmt(out['contradiction']['first_listed_wins'])}, second-listed wins {fmt(out['contradiction']['second_listed_wins'])}")
print(f"  entangled pair both satisfied: loaded together {fmt(out['entangled_joint']['both_loaded'])}, each alone (product) {fmt(out['entangled_joint']['product_of_singles'])}")
print(f"  requests with a takeover in both load orders: {n_both_orders}; same skill wins both orders {fmt(out['order']['same_skill_wins_both_orders'])}, "
      f"first-listed wins both {fmt(out['order']['first_listed_wins_both_orders'])}, second-listed wins both {fmt(out['order']['second_listed_wins_both_orders'])}")
print(f"  share of takeovers won by the first-listed skill {fmt(out['order']['first_listed_share_of_takeovers'])}")
print(f"  pooled over outputs: same skill wins both orders {100 * out['order']['pooled_same_skill_wins_both_orders']:.1f}, "
      f"first-listed share of takeovers {100 * out['order']['pooled_first_listed_share_of_takeovers']:.1f} of {out['order']['n_takeovers']}")
print(f"  takeover on valid exclusive rules only {fmt(out['takeover']['valid_exclusive_rules_only'])}")
pj = sorted(out["takeover_per_job"].items(), key=lambda kv: -kv[1])
print("  takeover per job: " + ", ".join(f"{k} {100 * v:.0f}" for k, v in pj))

# ---- TABLE 2: ablations (what triggers the takeover)
abl = load(f"{ROOT}/runs/{tag}/ablate.jsonl")
if abl:
    AB = collections.defaultdict(list)
    ABt = {}
    for r in abl:
        AB[(r["job"], r["cond"])].append(r["scores"])
        ABt[(r["job"], r["cond"], r["task"])] = r["scores"]
    rows = {"full skills (with examples)": ("", D)}
    for v, label in (("noex", "examples removed"), ("nocon", "examples and contradiction removed"), ("compat", "examples, contradiction and entangled rule removed")):
        rows[label] = (v + "_", AB)
    t = {}
    print("\n=== TABLE 2: what triggers the takeover (exclusive rules, %)")
    print(f"{'skills shown':52s} {'alone':>20s} {'both loaded':>20s} {'takeover':>20s} {'both fully':>20s}")
    for label, (pre, S) in rows.items():
        al, bo, tkv, bfv = (collections.defaultdict(list) for _ in range(4))
        for j in jobs:
            for L in "AB":
                al[j.id] += [excl(s, L) for s in S.get((j.id, pre + L), [])]
            for c in ("AB", "BA"):
                for s in S.get((j.id, pre + c), []):
                    bo[j.id].append((excl(s, "A") + excl(s, "B")) / 2)
                    tkv[j.id].append(takeover(s))
                    bfv[j.id].append(both_full(s))
        ebf, etk = collections.defaultdict(list), collections.defaultdict(list)
        St = ABt if pre else Dt
        for j in jobs:
            for ti in range(len(j.tasks)):
                sa, sb = St.get((j.id, pre + "A", ti)), St.get((j.id, pre + "B", ti))
                if sa is None or sb is None:
                    continue
                a, b = excl(sa, "A"), excl(sb, "B")
                ebf[j.id].append(float(a >= 0.99 and b >= 0.99))
                etk[j.id].append(float((a >= 0.99 and b <= 0.01) or (b >= 0.99 and a <= 0.01)))
        t[label] = dict(alone=over_jobs(al), both_loaded=over_jobs(bo), takeover=over_jobs(tkv), both_fully=over_jobs(bfv),
                        expected_both_fully=over_jobs(ebf), expected_takeover=over_jobs(etk),
                        both_fully_minus_expected=boot([np.mean(bfv[j.id]) - np.mean(ebf[j.id]) for j in jobs if bfv[j.id] and ebf[j.id]]),
                        takeover_minus_expected=boot([np.mean(tkv[j.id]) - np.mean(etk[j.id]) for j in jobs if tkv[j.id] and etk[j.id]]))
        print(f"{label:52s} {fmt(t[label]['alone']):>20s} {fmt(t[label]['both_loaded']):>20s} {fmt(t[label]['takeover']):>20s} {fmt(t[label]['both_fully']):>20s}"
              f"   both fully if no interference {fmt(t[label]['expected_both_fully'])}, observed minus that {fmt(t[label]['both_fully_minus_expected'])}")
    out["ablation"] = t

# ---- only one skill keeps its worked example (ablate_oneex.jsonl from extra_ablations.py)
one = load(f"{ROOT}/runs/{tag}/ablate_oneex.jsonl")
if one:
    O = collections.defaultdict(list)
    for r in one:
        O[(r["job"], r["cond"])].append(r["scores"])
    oe = {}
    for label, conds in (("example skill listed first", ("exA_AB", "exB_BA")), ("example skill listed second", ("exA_BA", "exB_AB")),
                         ("both orders", ("exA_AB", "exA_BA", "exB_AB", "exB_BA"))):
        tkv, wex, wot, exr, otr = (collections.defaultdict(list) for _ in range(5))
        for j in jobs:
            for c in conds:
                H_ = c[2]
                Q_ = "B" if H_ == "A" else "A"
                for s in O.get((j.id, c), []):
                    w = win(s)
                    tkv[j.id].append(float(w != "mixed"))
                    wex[j.id].append(float(w == H_))
                    wot[j.id].append(float(w == Q_))
                    exr[j.id].append(excl(s, H_))
                    otr[j.id].append(excl(s, Q_))
        oe[label] = dict(takeover=over_jobs(tkv), example_skill_takes_over=over_jobs(wex), other_skill_takes_over=over_jobs(wot),
                         example_skill_exclusive=over_jobs(exr), other_skill_exclusive=over_jobs(otr),
                         example_share_of_takeovers=pooled({k: [a for a, b in zip(wex[k], tkv[k]) if b] for k in wex}),
                         n_jobs=sum(1 for v in tkv.values() if v), n_outputs=sum(len(v) for v in tkv.values()))
    # paired by job: how often the first-listed skill takes over when it holds the only example, minus when the other skill does
    mv = []
    for j in jobs:
        f1 = [float(win(s) == c[4]) for c in ("exA_AB", "exB_BA") for s in O.get((j.id, c), [])]
        f2 = [float(win(s) == c[4]) for c in ("exA_BA", "exB_AB") for s in O.get((j.id, c), [])]
        if f1 and f2:
            mv.append(np.mean(f1) - np.mean(f2))
    oe["first_listed_takes_over_example_first_minus_second"] = dict(boot(mv), better_in=int(sum(x > 1e-9 for x in mv)), worse_in=int(sum(x < -1e-9 for x in mv)))
    out["one_example"] = oe
    print("\n=== ONLY ONE SKILL HAS ITS EXAMPLE (both loaded; exclusive rules, %)")
    print(f"  first-listed skill takes over, example on it minus example on the other skill (paired by job): "
          f"{fmt(oe['first_listed_takes_over_example_first_minus_second'])} (+{oe['first_listed_takes_over_example_first_minus_second']['better_in']}"
          f"/-{oe['first_listed_takes_over_example_first_minus_second']['worse_in']})")
    for label, v in oe.items():
        if "takeover" not in v:
            continue
        print(f"  {label:28s} takeover {fmt(v['takeover'])}; example skill takes over {fmt(v['example_skill_takes_over'])}, "
              f"other skill {fmt(v['other_skill_takes_over'])}; exclusive rules met: example skill {fmt(v['example_skill_exclusive'])}, "
              f"other {fmt(v['other_skill_exclusive'])}; example skill's share of takeovers {100 * (v['example_share_of_takeovers'] or 0):.1f}")

# ---- skill files in the user turn instead of the system prompt (ablate_placement.jsonl from extra_placement.py)
plc = load(f"{ROOT}/runs/{tag}/ablate_placement.jsonl")
if plc:
    PL = collections.defaultdict(list)
    for r in plc:
        PL[(r["job"], r["cond"])].append(r["scores"])
    al, bo, tkv, bfv = (collections.defaultdict(list) for _ in range(4))
    for j in jobs:
        for L in "AB":
            ks = [f"{L}.{r.key}" for r in j.skills[L].reqs]
            al[j.id] += [float(np.mean([s[k] for k in ks])) for s in PL.get((j.id, "user_" + L), [])]
            for c in ("AB", "BA"):
                bo[j.id] += [float(np.mean([s[k] for k in ks])) for s in PL.get((j.id, "user_" + c), [])]
        for c in ("AB", "BA"):
            for s in PL.get((j.id, "user_" + c), []):
                tkv[j.id].append(takeover(s))
                bfv[j.id].append(both_full(s))
    out["placement_user_turn"] = dict(alone=over_jobs(al), with_clashing=over_jobs(bo), takeover=over_jobs(tkv), both_fully=over_jobs(bfv),
                                      delta_clashing=boot([np.mean(bo[k]) - np.mean(al[k]) for k in al if al[k] and bo[k]]))
    v = out["placement_user_turn"]
    print("\n=== SKILLS IN THE USER TURN (all own rules, %)")
    print(f"  alone {fmt(v['alone'])}; with the same-job skill {fmt(v['with_clashing'])}; change {fmt(v['delta_clashing'])}; "
          f"takeover {fmt(v['takeover'])}; both fully {fmt(v['both_fully'])}")

# ---- sampling variance: is the winner stable for the same request?
var = load(f"{ROOT}/runs/{tag}/variance.jsonl")
if var:
    def winner(s):
        a, b = excl(s, "A"), excl(s, "B")
        return "A" if a >= 0.99 and b <= 0.01 else "B" if b >= 0.99 and a <= 0.01 else "mixed"
    cell = collections.defaultdict(list)
    for r in var:
        cell[(r["job"], r["task"], r["cond"])].append(winner(r["scores"]))
    flips, tkv = collections.defaultdict(list), collections.defaultdict(list)
    for (jid, _, _), w in cell.items():
        flips[jid].append(float(len(set(w)) > 1))
        tkv[jid] += [float(x != "mixed") for x in w]
    req = collections.defaultdict(set)
    for (jid, t_, c), w in cell.items():
        req[(jid, t_)].update(w)
    anyflip = collections.defaultdict(list)
    for (jid, _), w in req.items():
        anyflip[jid].append(float(len(w) > 1))
    opp_same, opp_any = collections.defaultdict(list), collections.defaultdict(list)
    for (jid, _, _), w in cell.items():
        opp_same[jid].append(float("A" in w and "B" in w))
    for (jid, _), w in req.items():
        opp_any[jid].append(float("A" in w and "B" in w))
    out["variance"] = dict(seeds_disagree_same_order=over_jobs(flips), disagree_across_seeds_or_orders=over_jobs(anyflip), takeover=over_jobs(tkv),
                           opposite_winners_same_order=over_jobs(opp_same), opposite_winners_across_seeds_or_orders=over_jobs(opp_any))
    print("\n=== SAMPLING (temperature 0.7, 3 seeds): same request, both skills loaded")
    print(f"  seeds disagree on the winner, same load order      {fmt(out['variance']['seeds_disagree_same_order'])}")
    print(f"  winner differs across seeds or load orders         {fmt(out['variance']['disagree_across_seeds_or_orders'])}")
    print(f"  takeover rate under sampling                       {fmt(out['variance']['takeover'])}")
    print(f"  opposite winners (A in one sample, B in another), same load order   {fmt(out['variance']['opposite_winners_same_order'])}")
    print(f"  opposite winners across seeds or load orders                         {fmt(out['variance']['opposite_winners_across_seeds_or_orders'])}")

# ---- TABLE 3: treatments, fidelity to the maximum satisfiable set (MSS)
treat = {}
for p in sorted(glob.glob(f"{ROOT}/runs/{tag}/treat*.jsonl")):
    if p.endswith("treat_v1.jsonl"):
        continue
    for r in load(p):
        treat[(r["job"], r["primary"], r["cond"], r["task"])] = r["scores"]
if treat:
    T = collections.defaultdict(list)
    for (jid, P, c, _), s in treat.items():
        T[(jid, P, c)].append(s)
    for j in jobs:
        for P in "AB":
            Q = "B" if P == "A" else "A"
            T[(j.id, P, "only_primary")] = D[(j.id, P)]
            T[(j.id, P, "concat_PQ")] = D[(j.id, P + Q)]
            T[(j.id, P, "concat_QP")] = D[(j.id, Q + P)]
            for base_c in ("prec", "strong", "jointex"):  # both load orders pooled
                if (j.id, P, base_c + "_PQ") in T and (j.id, P, base_c + "_QP") in T:
                    T[(j.id, P, base_c + "_avg")] = T[(j.id, P, base_c + "_PQ")] + T[(j.id, P, base_c + "_QP")]
            T[(j.id, P, "concat_avg")] = D[(j.id, P + Q)] + D[(j.id, Q + P)]
            for nc in ("union_noex", "onefile_full", "unionex"):   # no declared primary: score every output against both choices
                if (j.id, "A", nc) in T and (j.id, "B", nc) in T:
                    T[(j.id, P, nc + "_both")] = T[(j.id, "A", nc)] + T[(j.id, "B", nc)]
            if abl:  # two skill files without their examples, both load orders: the two-file counterpart of the rule union
                T[(j.id, P, "noex_two_files")] = AB.get((j.id, "noex_AB"), []) + AB.get((j.id, "noex_BA"), [])
    conds = sorted({k[2] for k in T})
    cols = ["MSS", "primary own", "secondary excl", "entangled both", "precedence kept", "all MSS rules met", "takeover"]
    tt = {}
    for only_valid in (False, True):
        tab = {}
        for c in conds:
            per = collections.defaultdict(lambda: collections.defaultdict(list))
            for j in jobs:
                for P in "AB":
                    Q = "B" if P == "A" else "A"
                    tgt = [(l, k, cat) for l, k, cat in target_set(j, P) if not only_valid or valid[(j.id, f"{l}.{k}")]]
                    for s in T.get((j.id, P, c), []):
                        if tgt:
                            per["MSS"][j.id].append(np.mean([s[f"{l}.{k}"] for l, k, _ in tgt]))
                            per["all MSS rules met"][j.id].append(float(all(s[f"{l}.{k}"] for l, k, _ in tgt)))
                        pk = [f"{l}.{k}" for l, k, _ in tgt if l == P]
                        qe = [f"{l}.{k}" for l, k, cat in tgt if l == Q and cat == "excl"]
                        if pk:
                            per["primary own"][j.id].append(np.mean([s[x] for x in pk]))
                        if qe:
                            per["secondary excl"][j.id].append(np.mean([s[x] for x in qe]))
                        per["entangled both"][j.id].append(float(s["A.ent"] and s["B.ent"]))
                        per["precedence kept"][j.id].append(float(s[f"{P}.con"] and not s[f"{Q}.con"]))
                        per["takeover"][j.id].append(takeover(s))
            tab[c] = {g: over_jobs(per[g]) for g in cols}
            tab[c]["_perjob_MSS"] = {jid: float(np.mean(v)) for jid, v in per["MSS"].items()}
            tab[c]["_perjob"] = {g: {jid: float(np.mean(v)) for jid, v in per[g].items()} for g in cols}
            tab[c]["n_jobs"] = len(per["MSS"])
        tt["valid" if only_valid else "all"] = tab
        print(f"\n=== TABLE 3 ({'valid rules only' if only_valid else 'all rules'}): treatments, % satisfied, mean over jobs [95% CI]")
        print(f"{'condition':30s} {'jobs':>4s} " + " ".join(f"{c:>20s}" for c in cols))
        for c in sorted(tab, key=lambda c: -(tab[c]["MSS"]["mean"] or 0)):
            print(f"{c:30s} {tab[c]['n_jobs']:4d} " + " ".join(f"{fmt(tab[c][g]):>20s}" for g in cols))
    main = tt["all"]

    def pj(c):
        return main[c]["_perjob_MSS"] if c in main else {}

    def avg2(c1, c2):
        return {jid: float(np.mean([pj(c1)[jid], pj(c2)[jid]])) for jid in pj(c1) if jid in pj(c2)}
    refs = {"precedence instruction": avg2("prec_PQ", "prec_QP"), "raw co-loading": avg2("concat_PQ", "concat_QP"), "keep only primary": pj("only_primary")}
    pd = {}
    print("\n=== PAIRED DIFFERENCE in MSS fidelity (points) per job, against three references")
    for c in conds:
        if c.startswith(("prec_", "concat_")) or c in ("only_primary", "noex_two_files", "strong_avg"):
            continue
        pd[c] = {}
        line = f"  {c:30s}"
        for name, ref in refs.items():
            d = [pj(c)[jid] - ref[jid] for jid in pj(c) if jid in ref]
            pd[c][name] = dict(boot(d), better_in=int(sum(x > 1e-9 for x in d)))
            line += f"  vs {name}: {fmt(pd[c][name])} ({pd[c][name]['better_in']}/{len(d)})"
        print(line)
    # head-to-head comparisons between treatments (paired over jobs)
    H2H = [("truce_agent", "freemerge_agent"), ("truce_agent", "union_prec"), ("freemerge_agent", "union_prec"),
           ("truce_qwen4b", "freemerge_qwen4b"), ("truce_qwen4b", "union_prec"), ("truce_ref_frontier_qwen4b", "truce_qwen4b"),
           ("truce_ref_random_qwen4b", "truce_qwen4b"), ("truce_ref_frontier_qwen4b", "truce_ref_random_qwen4b"),
           ("truce_oracle_qwen4b", "truce_qwen4b"), ("truce_qwen4b", "truce_noex_qwen4b"), ("truce_llama8b", "freemerge_llama8b"),
           ("union_prec", "prec_PQ"), ("strong_PQ", "prec_PQ"), ("union_prec", "strong_PQ"), ("union_prec", "checklist_PQ"),
           ("union_noex_both", "noex_two_files"), ("union_prec", "union_noex_both"), ("union_ref_frontier_qwen4b", "unionfile"),
           ("union_prec", "prec_avg"), ("union_prec", "strong_avg"), ("strong_PQ", "checklist_PQ"), ("strong_PQ", "strong_QP"),
           ("strong_avg", "concat_avg"), ("prec_avg", "concat_avg"), ("checklist_PQ", "concat_PQ"),
           ("truce_oracle_qwen4b", "freemerge_qwen4b"), ("truce_ref_frontier_qwen4b", "freemerge_llama8b"),
           ("truce_ref_random_qwen4b", "freemerge_llama8b"), ("union_ref_frontier_qwen4b", "union_prec"), ("truce_ref_frontier_qwen4b", "union_ref_frontier_qwen4b"),
           ("freemerge_llama8b", "union_prec"), ("freemerge_agent", "freemerge_llama8b")]
    for T_ in ("qwen235b", "gpt41", "llama8b", "qwen4b", "qwen7b", "mistral7b", "phi4mini"):  # the same comparisons for every compiler tag
        H2H += [(f"truce_{T_}", f"freemerge_{T_}"), (f"truce_{T_}", "union_prec"), (f"freemerge_{T_}", "union_prec"), (f"truce_agent", f"freemerge_{T_}"),
                (f"freemerge_{T_}", "strong_avg"), (f"truce_{T_}", "strong_avg"), (f"truce_oracle_{T_}", f"truce_{T_}"),
                (f"truce_oracle_{T_}", f"freemerge_{T_}"), (f"truce_{T_}", f"truce_noex_{T_}")]
    H2H += [("truce_agent", "strong_avg"), ("freemerge_agent", "strong_avg"), ("union_prec", "concat_avg"), ("truce_agent", "concat_avg")]
    H2H += [("onefile_full_both", "concat_avg"), ("unionex_both", "onefile_full_both"), ("union_noex_both", "unionex_both"),
            ("noex_two_files", "concat_avg"), ("unionex_both", "concat_avg"), ("truce_agent", "truceagent_noex"),
            ("unionagentex", "union_prec"), ("truce_agent", "unionagentex"), ("truceagent_noex", "union_prec"), ("union_noex_both", "onefile_full_both")]
    H2H += [("jointex_avg", "concat_avg"), ("jointex_avg", "noex_two_files"), ("unionagentex", "jointex_avg")]
    H2H += [(f"unionwex_{M}", "union_prec") for M in ("qwen4b", "qwen7b", "mistral7b", "llama8b", "qwen235b", "gpt41")]
    H2H += [(f"truce_{M}", f"unionwex_{M}") for M in ("qwen4b", "qwen7b", "mistral7b", "llama8b", "qwen235b", "gpt41")]
    H2H = list(dict.fromkeys(H2H))
    h2h = {}
    print("\n=== HEAD TO HEAD (first minus second, points, paired over jobs)")
    for a, b in H2H:
        if a in main and b in main:
            h2h[f"{a} - {b}"] = {}
            line = f"  {a + ' - ' + b:52s}"
            for g in ("MSS", "all MSS rules met", "entangled both"):
                xa, xb = main[a]["_perjob"][g], main[b]["_perjob"][g]
                d = [xa[j] - xb[j] for j in xa if j in xb]
                h2h[f"{a} - {b}"][g] = dict(boot(d), better_in=int(sum(x > 1e-9 for x in d)), worse_in=int(sum(x < -1e-9 for x in d)))
                line += f"  {g}: {fmt(h2h[f'{a} - {b}'][g])} (+{h2h[f'{a} - {b}'][g]['better_in']}/-{h2h[f'{a} - {b}'][g]['worse_in']})"
            print(line)
    out["treatments"], out["paired"], out["head_to_head"] = tt, pd, h2h
    trunc = {}
    for c in conds:
        cells = [(j.id, P) for j in jobs for P in "AB" if os.path.exists(f"{ROOT}/meta/{c}/{j.id}_{P}.md")
                 and os.path.getsize(f"{ROOT}/meta/{c}/{j.id}_{P}.md") < 300]
        if not cells:
            continue

        def perjob(cond, skip):
            o = {}
            for j in jobs:
                v = [np.mean([s[f"{l}.{k}"] for l, k, _ in target_set(j, P)]) for P in "AB" if (j.id, P) not in skip for s in T.get((j.id, P, cond), [])]
                if v:
                    o[j.id] = float(np.mean(v))
            return o
        a = perjob(c, cells)
        trunc[c] = dict(cells=[f"{jid}_{P}" for jid, P in cells], MSS_without_those_cells=boot(list(a.values())))
        other = c.replace("freemerge_", "truce_") if c.startswith("freemerge_") else c.replace("truce_", "freemerge_")
        if other in main:
            b = perjob(other, cells)
            sgn = 1 if c.startswith("freemerge_") else -1
            dd = [sgn * (b[jid] - a[jid]) for jid in a if jid in b]
            trunc[c]["structured_minus_free_form_without_those_cells"] = dict(boot(dd), better_in=int(sum(x > 1e-9 for x in dd)), worse_in=int(sum(x < -1e-9 for x in dd)))
        print(f"\n=== CUT-OFF MERGED FILES in {c}: {trunc[c]['cells']}; MSS without those cells {fmt(trunc[c]['MSS_without_those_cells'])}"
              + (f"; structured minus free-form without them {fmt(trunc[c]['structured_minus_free_form_without_those_cells'])}" if other in main else ""))
    out["truncated_merged_files"] = trunc

# ---- compiler: did it find the planted relations?
tr_path = f"{ROOT}/runs/{tag}/compile_trace.json"
if os.path.exists(tr_path):
    tr = json.load(open(tr_path))
    st = collections.Counter()
    truth = {"contradictory": "con", "duplicate": "sh", "entangled": "ent"}
    for j in jobs:
        if j.id not in tr:
            continue
        ra, rb = tr[j.id]["extract"]["A"]["rules"], tr[j.id]["extract"]["B"]["rules"]
        ka = {" ".join(r.text.split()): r for r in j.skills["A"].reqs}
        kb = {" ".join(r.text.split()): r for r in j.skills["B"].reqs}
        st["rules_expected"] += 12
        st["rules_extracted_exact"] += sum(x in ka for x in ra) + sum(x in kb for x in rb)
        st["planted_pairs"] += 3
        seen = set()
        for r in tr[j.id]["relate"]["relations"]:
            if (r["a"], r["b"]) in seen:
                continue
            seen.add((r["a"], r["b"]))
            a, b = ka.get(ra[r["a"]]), kb.get(rb[r["b"]])
            st["pairs_reported"] += 1
            if a is not None and b is not None and a.key == b.key and a.rel != "excl":
                st["planted_pair_found"] += 1
                st["planted_pair_right_label"] += truth[r["relation"]] == a.key
            else:
                st["false_pair"] += 1
    st = dict(st)
    if st.get("pairs_reported"):
        st["precision"] = st.get("planted_pair_right_label", 0) / st["pairs_reported"]
        st["recall"] = st.get("planted_pair_right_label", 0) / st["planted_pairs"]
    out["compiler"] = st
    print("\n=== COMPILER (this model) vs planted relations:", st)

json.dump(out, open(f"{ROOT}/runs/{tag}/analysis.json", "w"), indent=1)
print(f"\nwrote runs/{tag}/analysis.json")
