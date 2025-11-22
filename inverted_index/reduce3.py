#!/usr/bin/env python3
import sys
import math

current_doc = None
terms = []
squared_sum = 0

for line in sys.stdin:
    docid, term_tf = line.strip().split("\t")
    term, tf = term_tf.split()
    tf = int(tf)

    if docid != current_doc:
        if current_doc is not None:
            print(f"{current_doc}\t{' '.join(terms)}")
        current_doc = docid
        terms = []

    terms.append(f"{term} {tf}")

# print last doc
if current_doc is not None:
    print(f"{current_doc}\t{' '.join(terms)}")
