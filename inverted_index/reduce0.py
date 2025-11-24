#!/usr/bin/env python3
"""Reduce 0: sum counts into total document count."""

import sys


def main() -> None:
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            total += int(line)
        except ValueError:
            continue
    print(total)


if __name__ == "__main__":
    main()
