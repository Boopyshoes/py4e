filename = input('Enter file name: ')
if filename == 'na na na boo boo':
    print('*blows raspberry*')
try:
    mailbox = open(filename,'r')
except:
    print('file not found:',filename)
    exit()
count = 0
total = 0
for line in mailbox:
    if line.startswith('X-DSPAM-Confidence'):
        colon_pos = line.find(':')
        line = line[colon_pos+1:].strip()
        try:
            total = total + float(line)
            count = count + 1
        except:
            continue

print('Average spam confidence:', total/count)
mailbox.close()
