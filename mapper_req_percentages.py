#!/usr/bin/env python
"""mapper_req_percentage.py"""

import sys
import re

def mapper():
  # we are going to use a regex method to find the request type in the row
  log_pattern = re.compile(r'\"(\w+)\s')  # this is the pattern to capture the method inside quotes

  for line in sys.stdin:
      # remove leading/trailing whitespace
      line = line.strip()
      # increment the Hadoop counter for total records
      print("reporter:counter:LogMetrics,TotalRecords,1")

      # use regex to search for the request type
      match = log_pattern.search(line) # search the line for a matching pattern
      if match:  # if it matches, that is the request_type
          request_type = match.group(1)
          # tab-delimited; the trivial type count is 1
          print '%s\t%s' % (request_type, 1)

if __name__ == "__main__":
    mapper()
