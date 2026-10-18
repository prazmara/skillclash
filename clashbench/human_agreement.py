#!/usr/bin/env python
"""Agreement of a human rater with the planted rule relations. Usage: python human_agreement.py human_validation/form_<name>.csv

The rater lists, per job, interacting rule pairs (A<i>, B<j>, relation) using the rule numbers of
human_validation/skill_pairs.md, which follow the order of the rules in the skill files (spec.rule_order).
Writes runs/human_<name>.json and prints a summary. The answer key is computed from the benchmark code.
"""
import collections
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from spec import rule_order  # noqa: E402
import jobs_core  # noqa: E402
import jobs_extra  # noqa: E402

JOBS = {j.id: j for j in list(jobs_core.JOBS) + list(jobs_extra.JOBS)}
NAME = {"duplicate": "sh", "contradictory": "con", "entangled": "ent"}
path = sys.argv[1]
rater = os.path.basename(path).replace("form_", "").replace(".csv", "").lower()

# planted pairs: (job, A index, B index) -> relation key, with 1-based indices in the order shown to the rater
planted = {}
for jid, j in JOBS.items():
    ia = {r.key: i + 1 for i, r in enumerate(rule_order(j.skills["A"], j))}
    ib = {r.key: i + 1 for i, r in enumerate(rule_order(j.skills["B"], j))}
    for k in ("con", "sh", "ent"):
        planted[(jid, ia[k], ib[k])] = k

rated = {}
for row in csv.reader(open(path)):
    if not row or row[0] == "job" or not row[1].strip():
        continue
    jid, a, b, rel = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip().lower()
    rated[(jid, int(a.lstrip("Aa")), int(b.lstrip("Bb")))] = NAME.get(rel, rel)

st = collections.Counter()
conf = collections.Counter()
for k, rel in planted.items():
    st["planted_" + rel] += 1
    if k in rated:
        st["found_" + rel] += 1
        st["same_label_" + rel] += rated[k] == rel
        conf[(rel, rated[k])] += 1
    else:
        conf[(rel, "not listed")] += 1
extra = {k: v for k, v in rated.items() if k not in planted}
out = dict(rater=rater, jobs=len(JOBS), planted_pairs=len(planted), rated_pairs=len(rated),
           planted_pairs_found=sum(k in rated for k in planted), same_label=sum(rated.get(k) == v for k, v in planted.items()),
           extra_pairs=len(extra), by_relation={r: dict(planted=st["planted_" + r], found=st["found_" + r], same_label=st["same_label_" + r]) for r in ("con", "sh", "ent")},
           confusion={f"{a} -> {b}": n for (a, b), n in sorted(conf.items())},
           extra=[dict(job=k[0], a=f"A{k[1]}", b=f"B{k[2]}", relation=v) for k, v in sorted(extra.items())])
json.dump(out, open(f"{ROOT}/runs/human_{rater}.json", "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "extra"}, indent=1))
print("pairs the rater listed that are not planted:", [(e["job"], e["a"], e["b"], e["relation"]) for e in out["extra"]])
