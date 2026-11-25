#!/usr/bin/env python3
"""The Absurd Clause Contest — entry generator (pure Python stdlib).

Validates the clause (one sentence, 1-200 chars, non-blank) and writes it
with NO trailing newline to entry.txt in MAKEFUN_OUTPUT_DIR (or /output,
with a local output/ fallback), file mode 0644, umask 022.
"""

import os
import sys

CLAUSE = (
    "Section 8.4: The User agrees that, upon termination, any remaining "
    "account balance shall be converted into pickles and mailed to the "
    "Company's registered office, postage due."
)


def main() -> int:
    clause = CLAUSE.strip()
    if not clause:
        print("error: clause is empty", file=sys.stderr)
        return 1
    if len(clause) > 200:
        print(f"error: clause is {len(clause)} chars, exceeds 200", file=sys.stderr)
        return 1
    if ". " in clause or not clause.endswith("."):
        print("error: clause must be exactly one sentence", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)

    old_umask = os.umask(0o022)
    try:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(clause)
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)

    print(f"Wrote {path} ({len(clause)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
