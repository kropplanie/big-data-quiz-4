#!/usr/bin/env python
import sys
import re

def main(argv):
    total_count = 0
    # Regular expression to match the HTTP request type
    pattern = re.compile(r'\"([A-Z]+) ')
    
    # Read lines from standard input
    for line in sys.stdin:
        # Find all request types in the line
        request_types = pattern.findall(line)
        
        # Increment the counter for each request type
        for request in request_types:
            total_count +=1
            
    # Emit the total count as a special key-value pair
    print(f"__TOTAL__\t{total_count}")
if __name__ == "__main__":
    main(sys.argv)
