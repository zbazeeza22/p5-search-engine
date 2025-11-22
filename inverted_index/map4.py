#!/usr/bin/env python3
import sys

for line in sys.stdin:
    docid, rest = line.strip().split("\t", 1)
    term_tf_pairs = rest.split()

    # iterate through term/tf pairs
    for i in range(0, len(term_tf_pairs), 2):
        term = term_tf_pairs[i]
        tf = term_tf_pairs[i+1]

        print(f"{term}\t{docid} {tf}")
