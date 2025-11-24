#!/usr/bin/env python3
"""Reduce 1: identity reducer for docid and cleaned text."""

import sys


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        print(line)


if __name__ == "__main__":
    main()
