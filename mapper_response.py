#!/usr/bin/env python
import sys
import re

def main(argv):
    total_count = 0
    # Regular expression to match the HTTP response code
    pattern = re.compile(r'"\s*(\d{3})\s')

    # Read lines from standard input
    for line in sys.stdin:
        # Find all response codes in the line
        response_codes = pattern.findall(line)
        
        # Increment the counter for each response code
        for response in response_codes:
            # Convert response code to integer for comparison
            response_code = int(response)
            
            # Map to correct category
            if response_code < 200:
                print(f"{'informational_responses'}\t1")
            elif response_code < 300:
                print(f"{'successful_responses'}\t1")
            elif response_code < 400:
                print(f"{'redirection_messages'}\t1")
            elif response_code < 500:
                print(f"{'client_error_responses'}\t1")
            else:
                print(f"{'server_error_responses'}\t1")

            total_count += 1
            
            # Use Hadoop's counter mechanism by writing to stderr
            # The format is: 
            #    <counter group name> <counter name> <increment>
            sys.stderr.write(f"reporter:counter:ResponseCodes,{response},1\n")
            
    # Emit the total count as a special key-value pair
    print(f"__TOTAL__\t{total_count}")

if __name__ == "__main__":
    main(sys.argv)
