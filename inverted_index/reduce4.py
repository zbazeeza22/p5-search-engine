#!/usr/bin/env python3
import sys
import math

# Load total document count
with open("total_document_count.txt") as f:
    N = int(f.read().strip())

current_term = None
postings = []

def flush_term(term, postings):
    df = len(postings)
    idf = math.log10(N / df)
    
    for docid, tf in postings:
        print(f"{docid}\t{term} {tf} {idf}")

for line in sys.stdin:
    term, rest = line.strip().split("\t")
    docid, tf = rest.split()
    
    if term != current_term:
        if current_term is not None:
            flush_term(current_term, postings)
        current_term = term
        postings = []
    
    postings.append((docid, tf))

if current_term is not None:
    flush_term(current_term, postings)
