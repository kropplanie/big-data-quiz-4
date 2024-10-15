#!/usr/bin/env python
import sys
import re

def main(argv):
    total_count = 0
    # Regular expression to match the HTTP request type
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    
    # Read lines from standard input
    for line in sys.stdin:
        # Find all request types in the line
        request_types = pattern.findall(line)
        
        # Increment the counter for each request type
        for request in request_types:
            # Emit the request type with a count of 1 for downstream processing
            print(f"{request}\t1")
            total_count +=1
            
            # Use Hadoop's counter mechanism by writing to stderr
            # The format is: 
            #    <counter group name> <counter name> <increment>
            sys.stderr.write(f"reporter:counter:RequestTypes,{request},1\n")
            
    # Emit the total count as a special key-value pair
    print(f"__TOTAL__\t{total_count}")
if __name__ == "__main__":
    main(sys.argv)
