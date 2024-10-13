#!/usr/bin/env python
import sys
import re

def main(argv):
    # Regular expression to match the HTTP request type
    pattern = re.compile(r'\"([A-Z]+) ')
    
    # Read lines from standard input
    for line in sys.stdin:
        # Find all request types in the line
        request_types = pattern.findall(line)
        
        # Increment the counter for each request type
        for request in request_types:
            # Emit the request type with a count of 1 for downstream processing
            print(f"{request}\t1")
            
            # Use Hadoop's counter mechanism by writing to stderr
            # The format is: 
            #    <counter group name> <counter name> <increment>
            sys.stderr.write(f"reporter:counter:RequestTypes,{request},1\n")

if __name__ == "__main__":
    main(sys.argv)
