# Python for Everyone
# Chapter 8 exercise 5
filename = input('Enter the mailbox file name: ')
try:
    mailbox = open(filename)
except:
    print('Mailbox not found:',filename)
    exit()

count = 0
for line in mailbox:
    words = line.split()
    # print('Debug:', words)
    if len(words) >= 3 and words[0] == 'From':
        print(words[1])
        count = count + 1

print("There were",count,"lines in the file with 'From' as the first word")
