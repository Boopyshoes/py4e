# Python for Everyone
# Chapter 11 exercise 1
# Create a grep-like program
import re

filename = input('Enter File Name: ')
try:
    fhand = open(filename,'r')
except:
    print('file not found:',filename)
    exit()

regexp = input('Enter regular expression: ')
count = 0
for line in fhand:
    if re.search(regexp,line):
        line = line.rstrip()
        print(line)
        count += 1

print(filename,'had',count,'lines that matched',regexp)
