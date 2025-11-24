#!/usr/bin/env python3
"""Map 0: emit '1' once per HTML document."""

import sys


def main() -> None:
    for line in sys.stdin:
        if "<!DOCTYPE html>" in line:
            sys.stdout.write("1\n")


if __name__ == "__main__":
    main()
