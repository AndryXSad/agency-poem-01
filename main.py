# agency-poem-01 entry (Python 3.13, standard library only).
#
# Writes one fixed poem about agency to /output/entry.txt.
# The poem is deterministic: the same bytes on every run, no network,
# no randomness, no input read. Outside the grader's container,
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The poem: a person hands their days to an agent, piece by piece,
# until the agent decides what the person would say -- and says it
# better. The turn: the person takes back not the work, but the
# wanting -- the pause, the doubt, the choice itself.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "I gave it first the little things \u2014",
    "the forms, the files, the tangled strings",
    "of work I used to do by hand.",
    "It learned them. Fast. It understands.",
    "",
    "Then larger things: the letter home,",
    "the turn of phrase, the warmth, the tone.",
    "It wrote them well. Too well, I thought,",
    "till one line came back, and caught",
    "",
    "my throat. My voice \u2014 but cleaner, surer,",
    "each sentence trimmed, each doubt made poorer.",
    "It had decided what I'd say",
    "and said it better anyway.",
    "",
    "So I took back the smallest part \u2014",
    "not the work, the wanting. The heart",
    "of choosing. The pause before I send,",
    "the doubt that says wait, think again.",
    "",
    "It does the doing. That is fine.",
    "I keep the rein. It keeps the road.",
]


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text("\n".join(POEM_LINES), encoding="utf-8")


if __name__ == "__main__":
    main()
