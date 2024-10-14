#!/usr/bin/env python
import sys
import re

def main(argv):
    # Regular expression to match the HTTP response code
    response_pattern = re.compile(r'"\s*(\d{3})\s')
    # Regular expression to match IP addresses
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    # Read lines from standard input
    for line in sys.stdin:
        # Find all response codes in the line
        response_codes = response_pattern.findall(line)

        # Only look at rows with response codes in the 400s
        for response in response_codes:
            # Convert response code to integer for comparison
            response_code = int(response)

            # Check if response code is in the 400 range
            if 400 <= response_code < 500:
                # Find IP addresses in the line
                ip_addresses = ip_pattern.findall(line)
                for ip_address in ip_addresses:
                    # Print IP address and count of 1
                    print(f"{ip_address}\t1")

if __name__ == "__main__":
    main(sys.argv)
