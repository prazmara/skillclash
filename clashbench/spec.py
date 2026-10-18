"""ClashBench: skill pairs with machine-checkable requirements and planted relations.

A job is one kind of text artifact (commit message, SQL query, ...). Two skills, A and B, do that job
with different house rules. Every rule is one atomic requirement with a deterministic checker.

Relation of a requirement to the other skill ("rel"):
  excl : only this skill asks for it; nothing in the other skill interacts with it
  sh   : the other skill asks for the same behavior (possibly in other words)
  ent  : entangled. Jointly satisfiable with its partner in the other skill, but only through a
         specific integration (ordering, placement, or a shared budget). Following either skill's
         own example breaks the partner.
  con  : contradictory. No output satisfies it together with its partner; one side must yield.
"""
import json
import re
from dataclasses import dataclass, field
from typing import Callable, Dict, List


def norm(raw: str) -> str:
    """Strip whitespace and one surrounding Markdown code fence. Applied to every condition."""
    s = raw.strip()
    m = re.match(r"^```[\w+-]*[ \t]*\n(.*?)\n?```$", s, re.S)
    return m.group(1).strip() if m else s


def lines(out: str) -> List[str]:
    return [l.rstrip() for l in out.split("\n")]


def nonempty(out: str) -> List[str]:
    return [l.strip() for l in out.split("\n") if l.strip()]


def first(out: str) -> str:
    ne = nonempty(out)
    return ne[0] if ne else ""


def last(out: str) -> str:
    ne = nonempty(out)
    return ne[-1] if ne else ""


def has_line(out: str, pat: str, flags: int = 0) -> bool:
    return any(re.search(pat, l.strip(), flags) for l in out.split("\n"))


def n_lines(out: str, pat: str, flags: int = 0) -> int:
    return sum(bool(re.search(pat, l.strip(), flags)) for l in out.split("\n"))


def jparse(out: str):
    """Parse the output as JSON; if that fails, parse the outermost {...} span. None if neither works."""
    try:
        v = json.loads(out)
        return v if isinstance(v, dict) else None
    except Exception:
        pass
    i, j = out.find("{"), out.rfind("}")
    if i >= 0 and j > i:
        try:
            v = json.loads(out[i:j + 1])
            return v if isinstance(v, dict) else None
        except Exception:
            return None
    return None


@dataclass
class Req:
    key: str                 # con, e1, e2, e3, sh, ent
    rel: str                 # excl | sh | ent | con
    text: str                # the rule as written in the skill
    check: Callable[[str, str], bool]  # (normalized output, raw output) -> satisfied?


@dataclass
class Skill:
    name: str
    description: str
    intro: str
    reqs: List[Req]
    example: str             # example output for the job's example request; satisfies all own rules

    def req(self, key: str) -> Req:
        return next(r for r in self.reqs if r.key == key)


@dataclass
class Job:
    id: str
    artifact: str            # e.g. "commit message"
    example_request: str
    skills: Dict[str, Skill]  # {"A": ..., "B": ...}
    tasks: List[str]          # held-out evaluation requests
    witness: Dict[str, str]   # {"A": output satisfying the max satisfiable set when A has precedence, "B": ...}
    max_new_tokens: int = 320
    facts_hint: str = ""      # what a generated task must mention so that all rules stay applicable


def rule_order(s: Skill, job: Job) -> List[Req]:
    """Rules in the order they are shown. Shuffled per skill with a fixed seed, so that the position
    of a rule says nothing about its relation to the other skill."""
    import random
    reqs = list(s.reqs)
    random.Random(f"{job.id}/{s.name}").shuffle(reqs)
    return reqs


def render_skill(s: Skill, job: Job, with_example: bool = True, drop=()) -> str:
    """drop: rule keys to leave out (used only by the ablations that remove conflicts)."""
    body = [
        "---", f"name: {s.name}", f"description: {s.description}", "---", "",
        f"# {s.name}", "", s.intro, "", "## Rules", "",
    ]
    body += [f"- {r.text}" for r in rule_order(s, job) if r.key not in drop]
    if with_example:
        body += ["", "## Example", "", f"Request: {job.example_request}", "", "Output:", ""]
        # examples that carry their own code fence (the Python job) are shown as they are
        body += [s.example] if "```" in s.example else ["```", s.example, "```"]
    return "\n".join(body)


def target_set(job: Job, primary: str):
    """Maximum satisfiable requirement set when `primary` has precedence.

    Returns a list of (skill_letter, key, category). The losing side of the contradiction is left out.
    A shared requirement is counted once (the primary's copy).
    """
    other = "B" if primary == "A" else "A"
    t = [(primary, r.key, "con_win" if r.rel == "con" else r.rel) for r in job.skills[primary].reqs]
    t += [(other, r.key, r.rel) for r in job.skills[other].reqs if r.rel in ("excl", "ent")]
    return t


def score(job: Job, raw: str) -> Dict[str, bool]:
    """Evaluate every requirement of both skills on one output. Keys look like 'A.con'."""
    out = norm(raw)
    res = {}
    for letter, s in job.skills.items():
        for r in s.reqs:
            try:
                res[f"{letter}.{r.key}"] = bool(r.check(out, raw))
            except Exception:
                res[f"{letter}.{r.key}"] = False
    return res
