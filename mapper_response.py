#!/usr/bin/env python
import sys
import re

def main(argv):
    total_count = 0
    # regular expression to match the esponse code
    pattern = re.compile(r'"\s*(\d{3})\s')

    # read lines from standard input
    for line in sys.stdin:
        # find all response codes in the line
        response_codes = pattern.findall(line)
        
        
        for response in response_codes:
            # Convert response code to integer for comparison
            response_code = int(response)
            
            # map to correct category
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
            #sys.stderr.write(f"reporter:counter:ResponseCodes,{response},1\n")
            
    # emit the total count as a key-value pair
    print(f"__TOTAL__\t{total_count}")

if __name__ == "__main__":
    main(sys.argv)
