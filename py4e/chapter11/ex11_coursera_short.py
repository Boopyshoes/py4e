# Python for Everyone
# Chapter 11
# Optional challenge to create a compact version of the exercise assignment
import re
print(sum([int(x) for x in re.findall('[0-9]+',open('regex_sum_124697.txt').read()) if int(x) > 10]))