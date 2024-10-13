#!/usr/bin/env python
"""reducer.py"""

import sys

current_word = None
current_count = 0
word = None
total_count = 0
word_counts = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Count was not a number, so silently ignore/discard this line
        continue

    # Check if this line contains the special total count
    if word == "__TOTAL__":
        total_count += count
        continue

    # This IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Store the count for the current word
            word_counts[current_word] = current_count

        current_count = count
        current_word = word

# Do not forget to output the last word if needed!
if current_word == word:
    word_counts[current_word] = current_count

# Calculate and print the percentage for each word
if total_count > 0:
    for word, count in word_counts.items():
        percentage = (count / total_count) * 100
        print(f'{word}\t{percentage:.2f}%')
else:
    print("Error: Total count is zero or not found.")
