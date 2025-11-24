#!/usr/bin/env python3
"""Map 4: identity mapper for docid, term, tf, idf."""

import sys


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        print(line)


if __name__ == "__main__":
    main()
