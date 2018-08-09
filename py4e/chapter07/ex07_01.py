# filename = 'mbox-short.txt'
filename = input('Enter file name:')
try:
    mailbox = open(filename,'r')
except:
    print('file not found:',filename)
    exit()

for line in mailbox:
    line = line.rstrip()
    print(line.upper())

mailbox.close()
