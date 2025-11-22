#!/usr/bin/env python3
import sys

for line in sys.stdin:
    docid, rest = line.strip().split("\t", 1)
    partition = int(docid) % 3
    print(f"{partition}\t{docid} {rest}")
