#!/usr/bin/env python3
import sys
import math
from collections import defaultdict

# We aggregate by docid to compute norms, then invert to output by term.
doc_data = defaultdict(list) # docid -> [(term, tf, idf), ...]

for line in sys.stdin:
    # Input: partition \t docid term tf idf
    _, rest = line.strip().split("\t", 1)
    parts = rest.split()
    
    docid = parts[0]
    term = parts[1]
    tf = int(parts[2])
    idf = float(parts[3])
    
    doc_data[docid].append((term, tf, idf))

# Compute norms and build inverted index structure for this partition
inverted_index = defaultdict(list) # term -> [(docid, tf, norm, idf), ...]

for docid, terms in doc_data.items():
    # Calculate norm for document
    squared_sum = sum((t[1] * t[2]) ** 2 for t in terms)
    norm = math.sqrt(squared_sum)
    
    for term, tf, idf in terms:
        inverted_index[term].append((docid, tf, norm, idf))

# Sort terms alphabetically
sorted_terms = sorted(inverted_index.keys())

for term in sorted_terms:
    postings = inverted_index[term]
    # idf is the same for all postings of this term (it came from reduce4)
    idf = postings[0][3]
    
    # Sort postings by docid
    postings.sort(key=lambda x: int(x[0]))
    
    out_parts = []
    for docid, tf, norm, _ in postings:
        out_parts.extend([docid, str(tf), str(norm)])
        
    print(term, idf, *out_parts)
