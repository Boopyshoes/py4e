# Python for Everyone
# Chapter 11 Coursera Assignment
import re
filename = input('Enter the filename: ')
try:
    fhand = open(filename, 'r')
except:
    print('file not found: ', filename)
    exit()

total = 0
count = 0
for line in fhand:
    s_numbers = re.findall('[0-9]+',line)
    for number in s_numbers:
        total += int(number)
        count += 1

print('there are',count,'matches')
print('the sum is',total)
