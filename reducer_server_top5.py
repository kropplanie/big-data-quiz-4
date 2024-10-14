#!/usr/bin/env python
import sys
import heapq

# Assuming the total count is passed as an environment variable or command-line argument
current_word = None
current_count = 0
word = None
top_n = 5
top_n_heap = []


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            
            # Add to heap if it's in top N or replace the smallest if necessary
            if len(top_n_heap) < top_n:
                heapq.heappush(top_n_heap, (current_count, current_word))
            else:
                # Check if we should replace the smallest
                if current_count > top_n_heap[0][0]:  # Compare with the smallest count in the heap
                    heapq.heappushpop(top_n_heap, (current_count, current_word))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if len(top_n_heap) < top_n:
        heapq.heappush(top_n_heap, (current_count, current_word))
    else:
        if current_count > top_n_heap[0][0]:  # Compare with the smallest count in the heap
            heapq.heappushpop(top_n_heap, (current_count, current_word))
            
# Output the top N elements sorted by count in descending order
top_elements = sorted(top_n_heap, key=lambda x: x[0], reverse=True)
for count, word in top_elements:
    print(f"{word}\t{count}")
