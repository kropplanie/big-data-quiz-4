#!/usr/bin/env python
import sys

# Assuming the total count is passed as an environment variable or command-line argument
total_count = int(sys.argv[1])
current_word = None
current_count = 0

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Count was not a number, so silently ignore/discard this line
        continue

    # This IF-switch only works because Hadoop sorts map output by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to STDOUT
            print('%s\t%s' % (current_word, (current_count / total_count) * 100))
        
        current_count = count
        current_word = word

# Do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, (current_count / total_count) * 100))
