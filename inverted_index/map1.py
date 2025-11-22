#!/usr/bin/env python3
import sys
import bs4
import re

# load stopwords once
STOPWORDS = set(line.strip() for line in open("stopwords.txt"))

HTML = ""
for line in sys.stdin:
    if "<!DOCTYPE html>" in line:
        HTML = line
    else:
        HTML += line

    if "</html>" not in line:
        continue

    soup = bs4.BeautifulSoup(HTML, "html.parser")
    doc_id = soup.find("meta", attrs={"eecs485_docid": True}).get("eecs485_docid")

    element = soup.find("html")
    content = element.get_text(separator=" ", strip=True)
    content = content.replace("\n", " ")

    # CLEAN
    content = content.casefold()
    content = re.sub(r"[^a-z0-9 ]+", "", content)
    terms = content.split()
    terms = [t for t in terms if t not in STOPWORDS]
    cleaned = " ".join(terms)

    # OUTPUT
    print(f"{doc_id}\t{cleaned}")
