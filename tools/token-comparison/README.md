# Token comparison

What PMB costs against prose and against a plain bullet list, measured rather
than asserted. The figures cited in the [Internet-Draft](../../../RFC/) come
from here.

```sh
pip install tiktoken
python tools/token-comparison/measure.py
```

## Method

Three documents, each written three ways — flowing prose, a conventional
bullet list, and PMB — with the claim set held constant across all three
(11, 7 and 8 claims). Document C is a control: a status report is nearly all
fact and almost no scaffolding, so PMB should gain little on it. If PMB won
big everywhere including C, the corpus would be rigged.

Two tokenizers, `cl100k_base` and `o200k_base`. They agree within one token
throughout.

**Test 2 is the one that matters.** In Test 1 the PMB versions are worded a
little more tersely than the bullet versions, which is a confound: PMB
encourages terse phrasing, but that is a property of the writing, not of the
notation. Test 2 removes it by holding the wording and indentation identical
and changing only the leading marker.

## Result

| | tokens | vs prose | vs bullets |
|---|---|---|---|
| Flowing prose | 512 | — | |
| Bullet list | 341 | −33% | — |
| PMB | 286 | −44% | −16% |
| PMB vs **same-worded** bullets | 298 | | **−4%** |

Savings track scaffolding density, as predicted: −50% on the deliberation
document, −26% on the status-report control.

## What this does and does not support

The notation itself is close to free. A marked line costs what a bullet costs;
the only real saving is that a neutral line needs no marker at all, which is
why the control — every line neutral — shows the largest strict-test gap at
−11.6%.

So the claim to make is **not** that PMB compresses text. Most of the −44%
comes from writing atomic claims, and any bullet list gets that too.

The claim that survives is that **PMB records the role of every line at a
bullet list's price.** A bullet list is equally cheap and encodes nothing
about what a line is doing. That is an argument about information per token,
not about compression, and unlike a raw percentage it does not fall over when
someone points at a bullet list.

## Extending this

The corpus is three documents written by one author, which is enough to show
the shape and not enough to be a benchmark — the draft says so. If you want a
stronger number, add documents in `corpus.py` (keep the claim count honest and
equal across formats) and re-run.
