#!/usr/bin/env python3
"""Map 1: parse HTML, clean text, remove stopwords, emit docid and text."""

import sys
import re
import bs4


STOPWORDS = set(line.strip() for line in open("stopwords.txt", encoding="utf-8"))


def clean_text(text: str) -> str:
    text = text.casefold()
    text = re.sub(r"[^a-z0-9 ]+", "", text)
    terms = text.split()
    terms = [t for t in terms if t and t not in STOPWORDS]
    return " ".join(terms)


def main() -> None:
    html = ""
    for line in sys.stdin:
        if "<!DOCTYPE html>" in line:
            html = line
        else:
            html += line

        if "</html>" not in line:
            continue

        soup = bs4.BeautifulSoup(html, "html.parser")
        meta = soup.find("meta", attrs={"eecs485_docid": True})
        docid = meta.get("eecs485_docid")

        element = soup.find("html")
        content = element.get_text(separator=" ", strip=True)
        content = content.replace("\n", " ")
        cleaned = clean_text(content)

        sys.stdout.write(f"{docid}\t{cleaned}\n")


if __name__ == "__main__":
    main()
