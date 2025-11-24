#!/usr/bin/env python3
"""Map 5: assign postings to segment based on docid % 3."""

import sys


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            term, rest = line.split("\t", 1)
        except ValueError:
            continue

        parts = rest.split()
        if len(parts) != 4:
            continue

        docid = parts[0]
        partition = int(docid) % 3
        sys.stdout.write(f"{partition}\t{term} {docid} {parts[1]} {parts[2]} {parts[3]}\n")


if __name__ == "__main__":
    main()
