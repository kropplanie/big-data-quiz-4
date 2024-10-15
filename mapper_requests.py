#!/usr/bin/env python
import sys
import re

def main(argv):
    total_count = 0
    # regular expression to match the request type
    pattern = re.compile(r'\"([A-Z]+) ')
    
    # read lines from standard input
    for line in sys.stdin:
        # find all request types in the line
        request_types = pattern.findall(line)
        
        # Increment the counter for each request type
        for request in request_types:
            # Emit the request type with a count of 1 for downstream processing
            print(f"{request}\t1")
            total_count +=1
            
            
    # print total count as a key-value pair
    print(f"__TOTAL__\t{total_count}")
if __name__ == "__main__":
    main(sys.argv)
