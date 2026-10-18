#!/usr/bin/env python
"""Code-only meta-skill variants for the file-versus-example ablation. Usage: python make_variants.py

Writes meta/<variant>/<job>_<P>.md (P = the skill listed first). Nothing here calls a model.
  onefile_full     both original skill files, examples included, inside ONE skill file (one front matter)
  unionex          the rule union of both skills (no precedence line) with both original examples added
  truceagent_noex  Claude Opus 5.5's step-by-step merged file with its example section removed
  unionagentex     the rule union with the precedence line (union_prec), plus the example section of Claude's merged file
  unionwex_<M>     the same, with the example section of merger M's step-by-step file (truce_<M>)
Together with the existing conditions this gives a 2 x 2 design: {two files, one file} x {examples, no examples}:
  two files + examples = concat (diag AB/BA), two files no examples = noex_two_files (ablate),
  one file + examples = onefile_full / unionex, one file no examples = union_noex.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import harness as H  # noqa: E402


def body(job, L):
    """A rendered skill file without its front matter."""
    t = H.skill_text(job, L)
    parts = t.split("---", 2)
    return parts[2].strip() if t.startswith("---") and len(parts) == 3 else t


def example_block(job, L):
    s = job.skills[L]
    out = [f"Example for `{s.name}`:", "", f"Request: {job.example_request}", "", "Output:", ""]
    out += [s.example] if "```" in s.example else ["```", s.example, "```"]
    return "\n".join(out)


for job in H.JOBS:
    for P in "AB":
        Q = "B" if P == "A" else "A"
        sp, sq = job.skills[P], job.skills[Q]
        one = "\n".join(["---", f"name: {sp.name}+{sq.name}",
                         f"description: One file that contains the skills `{sp.name}` and `{sq.name}`. Use for any {job.artifact}.",
                         "---", "", body(job, P), "", body(job, Q)])
        H.save_meta("onefile_full", job, P, one, dict(method="both full skills in one file", first=P))
        uni = H.union_skill(job, P) + "\n\n## Examples\n\n" + example_block(job, P) + "\n\n" + example_block(job, Q)
        H.save_meta("unionex", job, P, uni, dict(method="rule union plus both original examples", first=P))
        m = H.load_meta("truce_agent", job, P)
        if m is not None:
            i = m.find("\n## Example")
            H.save_meta("truceagent_noex", job, P, (m[:i] if i >= 0 else m).rstrip(), dict(method="truce_agent with the example removed", primary=P))
            if i >= 0:
                H.save_meta("unionagentex", job, P, H.union_skill(job, P, precedence=True) + "\n" + m[i:].rstrip(),
                            dict(method="union_prec plus the example section of truce_agent", primary=P))
        for M in ("qwen4b", "qwen7b", "mistral7b", "llama8b", "qwen235b", "gpt41"):   # the same, with each merger's own example
            mm = H.load_meta(f"truce_{M}", job, P)
            k = mm.find("\n## Example") if mm is not None else -1
            if k >= 0:
                H.save_meta(f"unionwex_{M}", job, P, H.union_skill(job, P, precedence=True) + "\n" + mm[k:].rstrip(),
                            dict(method=f"union_prec plus the example section of truce_{M}", primary=P))
print("wrote meta/onefile_full, meta/unionex, meta/truceagent_noex, meta/unionagentex, meta/unionwex_<merger>")
