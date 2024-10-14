import sys
import heapq

top_n = 5  # Number of top elements to keep
top_n_heap = []  # Use a more descriptive name for the heap

current_word = None
current_count = 0

for line in sys.stdin:
    try:
        # Process each line of input (word, count)
        word, count = line.strip().split('\t')
        count = int(count)
    except ValueError:
        continue  # Skip lines that do not conform to the expected format

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

        current_word = word
        current_count = count

# Handle the last word
if current_word:
    if len(top_n_heap) < top_n:
        heapq.heappush(top_n_heap, (current_count, current_word))
    else:
        if current_count > top_n_heap[0][0]:  # Compare with the smallest count in the heap
            heapq.heappushpop(top_n_heap, (current_count, current_word))

# Output the top N elements sorted by count in descending order
top_elements = sorted(top_n_heap, key=lambda x: x[0], reverse=True)
for count, word in top_elements:
    print(f"{word}\t{count}")
