#!/usr/bin/env python
"""mapper_req_percentage.py"""

import sys, re

def main(argv):
  # we are going to use a regex method to find the request type in the row
  line = sys.stdin.readline()
  pattern = re.compile(r'\"(\w+)\s')  # this is the pattern to capture the method inside quotes
  
  try:
      while line:
          for request_type in pattern.findall(line):
              print("reporter:counter:LogMetrics,TotalRecords,1")
              print '%s\t%s' % (request_type, 1)
          line = sys.stdin.readline()
  except EOFError as error:
      return None

if __name__ == "__main__":
    main(sys.argv)



