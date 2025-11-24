#!/usr/bin/env python3
"""Reduce 3: compute idf per term and emit docid, term, tf, idf."""

import sys
import math


def flush_term(term: str, postings: list, total_docs: int) -> None:
    if not postings:
        return
    df = len(postings)
    idf = math.log10(total_docs / df)
    for docid, tf in postings:
        sys.stdout.write(f"{docid}\t{term} {tf} {idf}\n")


def main() -> None:
    with open("total_document_count.txt", encoding="utf-8") as f:
        total_docs = int(f.read().strip())

    current_term = None
    postings = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            term, rest = line.split("\t", 1)
        except ValueError:
            continue
        try:
            docid, tf = rest.split()
        except ValueError:
            continue

        if term != current_term:
            if current_term is not None:
                flush_term(current_term, postings, total_docs)
            current_term = term
            postings = []

        postings.append((docid, int(tf)))

    if current_term is not None:
        flush_term(current_term, postings, total_docs)


if __name__ == "__main__":
    main()
