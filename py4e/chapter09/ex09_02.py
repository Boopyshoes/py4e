# Python for Everyone
# Chapter 9 exercise 2
filename = input("Enter the mailbox file name: ")
try:
    mailbox = open(filename,'r')
except:
    print("file not found:",filename)
    exit()

days = dict()
for line in mailbox:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        days[words[2]] = days.get(words[2],0) + 1

print(days)
