#!/usr/bin/env python
import sys

def main():
    for line in sys.stdin:
        for word in line.strip().split():
            print(f"{word.lower()}\t1")

if __name__ == "__main__":
    main()
