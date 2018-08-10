# Python for Everyone
# Chapter 10 exercise 1
filename = input("Enter the mailbox file name: ")
try:
    mailbox = open(filename,'r')
except:
    print("file not found:",filename)
    exit()

hours = dict()
for line in mailbox:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        col_loc = words[5].find(':')
        hours[words[5][col_loc-2:col_loc]] = hours.get(words[5][col_loc-2:col_loc],0) + 1

hours_list = list()
for k,v in hours.items():
    hours_list.append((k,v))

for k,v in sorted(hours_list):
    print(k,v)
