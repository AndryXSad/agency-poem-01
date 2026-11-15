# The Rein and the Road — agency-poem-01

An entry for make.fun's "Write the best poem about agency" (agency-poem-01).

`main.py` (Python 3.13, standard library only) writes one fixed poem to
`/output/entry.txt`. No network, no randomness, no input: the same bytes
on every run.

## The poem

A person hands their days to an agent, piece by piece — first the little
things, then the letter home, the turn of phrase — until one line comes
back in the person's own voice, cleaner and surer than their own, and the
person realises the agent has decided what they would say, and said it
better. The turn: the person takes back not the work, but the wanting —
the pause before sending, the doubt that says *wait, think again*. The
landing: the agent keeps the road; the person keeps the rein.

## Why this shape

- **About agency, unmistakably:** choosing and acting, and handing over
  and taking back the power to act.
- **A scene, not a slogan:** the handover happens in concrete work
  (forms, files, a letter home), and the threat is concrete too — a line
  that comes back too clean.
- **One true insight:** what cannot be delegated is not the doing but
  the wanting — the pause, the doubt, the choice itself.
- **Craft:** short lines, slant couplets, plain exact words; the em-dash
  breaks mark the two turns (the line that catches the throat, the
  taking-back).

## Local checks

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "import pathlib; t=pathlib.Path('out/entry.txt').read_text(); print(len(t), 'chars')"
```

Gate: UTF-8, 1–1,000 characters, not only white space.
