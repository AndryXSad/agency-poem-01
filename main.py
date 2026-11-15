# agency-poem-01 entry v2 (Python 3.13, standard library only).
#
# Writes one fixed poem about agency to /output/entry.txt.
# The poem is deterministic: the same bytes on every run, no network,
# no randomness, no input read. Outside the grader's container,
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The poem ("The Wrong Stamp"): the agent writes the narrator's letters
# perfectly; when his oldest friend loses his wife, the narrator throws
# the agent's flawless draft away and writes it himself, by hand, with
# crossed-out lines, a misspelled word, the wrong stamp. The friend
# recognises him through the mistakes. The turn: the imperfection is
# the signature -- the one thing the agent cannot do is get it wrong
# the way a person does.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "The Wrong Stamp",
    "",
    "The agent writes my letters now \u2014",
    "thank-yous, condolences, birthday cards,",
    "in a hand I barely know as mine,",
    "every comma where it should be.",
    "",
    "Last week my oldest friend lost his wife of fifty years.",
    "The agent drafted it in a minute: warm, measured, right.",
    "Fifty years, it wrote. A life well lived.",
    "I read it twice and threw it away.",
    "",
    "I took a pen and wrote it myself.",
    "Crossed out three lines. Misspelled sorrow",
    "and left it. Licked the wrong stamp,",
    "walked to the box in the rain to post it.",
    "",
    "He called on Sunday, his voice thin.",
    "He said, I could tell it was you.",
]


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text("\n".join(POEM_LINES), encoding="utf-8")


if __name__ == "__main__":
    main()
