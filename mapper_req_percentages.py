#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile(r'\"(\w+)\s')
    try:
        while line:
            for req_type in pattern.findall(line):
                print (req_type.lower() + "\t" + "1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)


