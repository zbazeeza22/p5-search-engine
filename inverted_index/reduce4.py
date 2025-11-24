#!/usr/bin/env python3
"""Reduce 4: compute document norms and emit term-keyed postings."""

import sys
import math


def flush_doc(docid: str, postings: list) -> None:
    if not postings:
        return
    squared_sum = 0.0
    for term, tf, idf in postings:
        weight = tf * idf
        squared_sum += weight * weight
    norm = math.sqrt(squared_sum)
    for term, tf, idf in postings:
        sys.stdout.write(f"{term}\t{docid} {tf} {norm} {idf}\n")


def main() -> None:
    current_docid = None
    postings = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            docid, rest = line.split("\t", 1)
        except ValueError:
            continue

        parts = rest.split()
        if len(parts) != 3:
            continue
        term = parts[0]
        try:
            tf = int(parts[1])
            idf = float(parts[2])
        except ValueError:
            continue

        if docid != current_docid:
            if current_docid is not None:
                flush_doc(current_docid, postings)
            current_docid = docid
            postings = []

        postings.append((term, tf, idf))

    if current_docid is not None:
        flush_doc(current_docid, postings)


if __name__ == "__main__":
    main()
