#!/usr/bin/env python

import sys
import heapq

top_n = 10  # Number of top elements to keep
heap = []

current_word = None
current_count = 0

for line in sys.stdin:
    # Process each line of input (word, count)
    word, count = line.strip().split('\t')
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Add to heap if it's in top N or replace the smallest if necessary
            if len(heap) < top_n:
                heapq.heappush(heap, (current_count, current_word))
            else:
                heapq.heappushpop(heap, (current_count, current_word))
        current_word = word
        current_count = count

# Handle the last word
if current_word:
    if len(heap) < top_n:
        heapq.heappush(heap, (current_count, current_word))
    else:
        heapq.heappushpop(heap, (current_count, current_word))

# Output the top N elements
for count, word in heap:
    print(f"{word}\t{count}")
