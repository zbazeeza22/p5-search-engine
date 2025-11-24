#!/usr/bin/env python3
"""Map 2: compute term frequencies per document."""

import sys
from collections import Counter


def main() -> None:
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue

        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        docid, text = parts
        if not text:
            sys.stdout.write(f"{docid}\t\n")
            continue

        terms = text.split()
        counts = Counter(terms)

        pieces = []
        for term, tf in counts.items():
            pieces.append(f"{term} {tf}")
        sys.stdout.write(f"{docid}\t{' '.join(pieces)}\n")


if __name__ == "__main__":
    main()
