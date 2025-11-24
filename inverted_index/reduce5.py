#!/usr/bin/env python3
"""Reduce 5: build final inverted index for one segment."""

import sys


def main() -> None:
    inverted = {}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            _, rest = line.split("\t", 1)
        except ValueError:
            continue

        parts = rest.split()
        if len(parts) != 5:
            continue

        term = parts[0]
        docid = parts[1]
        tf = parts[2]
        norm = parts[3]
        idf = float(parts[4])

        if term not in inverted:
            inverted[term] = {"idf": idf, "postings": []}
        inverted[term]["postings"].append((docid, tf, norm))

    for term in sorted(inverted.keys()):
        idf = inverted[term]["idf"]
        postings = inverted[term]["postings"]
        postings.sort(key=lambda x: x[0])

        out_parts = [term, str(idf)]
        for docid, tf, norm in postings:
            out_parts.extend([docid, tf, norm])

        print(" ".join(out_parts))


if __name__ == "__main__":
    main()
