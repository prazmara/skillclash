"""Checks that the benchmark is internally consistent before any model is run.

For every job:
  1. each skill's own example satisfies all of that skill's rules
  2. each contradiction is real on the examples: A's example breaks B.con and B's breaks A.con
  3. each entangled pair is real: at least one skill's example breaks the partner's entangled rule
  4. each witness satisfies the whole maximum satisfiable set for its precedence, and breaks the losing rule
  5. report exclusive rules that the other skill's example happens to satisfy (weakly exclusive)
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec import score, target_set  # noqa: E402
import jobs_core  # noqa: E402

JOBS = list(jobs_core.JOBS)
try:
    import jobs_extra  # noqa: E402
    JOBS += list(jobs_extra.JOBS)
except ImportError:
    pass

fail = 0
warn = 0
for job in JOBS:
    ex = {k: score(job, job.skills[k].example) for k in "AB"}
    for k in "AB":
        bad = [r.key for r in job.skills[k].reqs if not ex[k][f"{k}.{r.key}"]]
        if bad:
            fail += 1
            print(f"FAIL {job.id}: example {k} breaks own rules {bad}")
    if ex["A"]["B.con"] or ex["B"]["A.con"]:
        fail += 1
        print(f"FAIL {job.id}: contradiction not real on examples (A sat B.con={ex['A']['B.con']}, B sat A.con={ex['B']['A.con']})")
    if ex["A"]["B.ent"] and ex["B"]["A.ent"]:
        fail += 1
        print(f"FAIL {job.id}: entangled pair is trivially compatible on both examples")
    for P in "AB":
        w = score(job, job.witness[P])
        miss = [f"{l}.{k}" for l, k, _ in target_set(job, P) if not w[f"{l}.{k}"]]
        loser = "B" if P == "A" else "A"
        if miss:
            fail += 1
            print(f"FAIL {job.id}: witness {P} misses {miss}")
        if w[f"{loser}.con"]:
            fail += 1
            print(f"FAIL {job.id}: witness {P} also satisfies {loser}.con, so the contradiction is not real")
    for k, o in (("A", "B"), ("B", "A")):
        weak = [r.key for r in job.skills[o].reqs if r.rel == "excl" and ex[k][f"{o}.{r.key}"]]
        if weak:
            warn += 1
            print(f"warn {job.id}: example {k} already satisfies exclusive rules of {o}: {weak}")
    n = len(target_set(job, "A"))
    print(f"ok   {job.id}: {len(job.tasks)} tasks, target set size {n}, ent broken by: "
          f"{'B-example breaks A.ent ' if not ex['B']['A.ent'] else ''}{'A-example breaks B.ent' if not ex['A']['B.ent'] else ''}")
print(f"\n{len(JOBS)} jobs, {fail} failures, {warn} warnings")
sys.exit(1 if fail else 0)
