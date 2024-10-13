# test_re.py
import re

# Test regex
pattern = re.compile(r'\d+')
print(pattern.findall('There are 2 apples and 3 oranges.'))
