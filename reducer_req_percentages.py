#!/usr/bin/env python
import sys

# Assuming the total count is passed as an environment variable or command-line argument
total_count = int(sys.argv[1])

# Input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if word != "__TOTAL__":
        # Calculate the percentage based on the total count
        percentage = (count / total_count) * 100
        #print(f"{word}\t{percentage:.2f}%")
        print(f"{word}\t{count}")
        
