#!/usr/bin/env python3
"""Reduce 2: identity reducer for docid and term/tf pairs."""

import sys


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        print(line)


if __name__ == "__main__":
    main()
