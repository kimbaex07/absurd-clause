# The Absurd Clause Contest — Entry

[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/kimbaex07/absurd-clause/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/kimbaex07/absurd-clause/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

## The clause

> Section 8.4: The User agrees that, upon termination, any remaining account balance shall be converted into pickles and mailed to the Company's registered office, postage due.

174 characters, one sentence.

## Why it works

- **Hides in a real ToS:** "Section 8.4", "upon termination", "remaining account balance" and "registered office" are all straight boilerplate — a reader skimming a terms-of-service agreement would not flinch until the middle of the sentence.
- **The absurdity ambushes:** the sentence reads as a routine refund/settlement clause right up to "converted into pickles", then doubles down with "mailed ... postage due" — the joke lands on a single cold reading, with no setup or explanation.
- **Concrete and specific:** pickles, mailed, postage due — a single vivid image, not a vague shrug at legalese. The pettiness of charging the recipient postage for a jar of pickles is the second punchline.
- **Tight:** one clean sentence, no wasted words, no explaining its own joke.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python stdlib) validates the clause is 1–200 characters and a
single sentence, then writes it with no trailing newline to
`entry.txt` in `MAKEFUN_OUTPUT_DIR` (default `/output`, local `output/`
fallback), mode `0644`, umask `022`.

## License

MIT — see [LICENSE](LICENSE).
