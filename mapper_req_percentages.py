#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile(r'\"([A-Z]+) ')
    try:
        while line:
            for word in pattern.findall(line):
                print (word.lower() + "\t" + "1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)

