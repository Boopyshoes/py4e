# Python for Everyone
# Chapter 11 exercise 1
# Create a program to
# 1)search a user-specified file for lines of the form 'New Revision: 39772',
# 2)extract the number from each of these lines
# 3)compute the average of these s_numbers
# 4)print the average
import re
regexp = '^New Revision:\s+([0-9]+)'

filename = input('Enter file name: ')
try:
    fhand = open(filename,'r')
except:
    print('file not found:',filename)
    exit()

number_list = list()
for line in fhand:
    line = line.rstrip()
    # print(line)
    line = re.findall(regexp,line)
    # print(line)
    if len(line) > 0:
        number_list.append(int(line[0]))

print(sum(number_list)/len(number_list))

number_list = [int(x) for x in re.findall('New Revision:\s+([0-9]+)\s',open(filename,'r').read())]
print(sum(number_list)/len(number_list))
