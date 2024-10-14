#!/usr/bin/env python
import sys
import re

def main(argv):
    total_count = 0
    # Regular expression to match the HTTP request type
    pattern = re.compile(r'\" [0-9]{3} ')
    
    # Read lines from standard input
    for line in sys.stdin:
        # Find all request types in the line
        response_codes = pattern.findall(line)
        
        # Increment the counter for each request type
        for response in response_codes:
            response = response.strip()
            # map to correct category
            if int(response) < 200:
                print(f"{'informational_responses'}\t1")
            elif int(response) < 300:
                print(f"{'successfull_responses'}\t1")
            elif int(response) < 400:
                print(f"{'redirection_messages'}\t1")
            elif int(response) < 500:
                print(f"{'client_error_responses'}\t1")
            else:
                print(f"{'server_error_responses'}\t1")

            total_count +=1
            
            # Use Hadoop's counter mechanism by writing to stderr
            # The format is: 
            #    <counter group name> <counter name> <increment>
            sys.stderr.write(f"reporter:counter:RequestTypes,{request},1\n")
            
    # Emit the total count as a special key-value pair
    print(f"__TOTAL__\t{total_count}")
if __name__ == "__main__":
    main(sys.argv)
