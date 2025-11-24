#!/usr/bin/env python3
"""Map 3: invert docid->terms into term->(docid, tf)."""

import sys


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            docid, rest = line.split("\t", 1)
        except ValueError:
            continue

        tokens = rest.split()
        if len(tokens) % 2 != 0:
            continue

        for i in range(0, len(tokens), 2):
            term = tokens[i]
            tf = tokens[i + 1]
            sys.stdout.write(f"{term}\t{docid} {tf}\n")


if __name__ == "__main__":
    main()
