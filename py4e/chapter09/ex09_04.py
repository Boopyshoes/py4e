# Python for Everyone
# Chapter 9 exercise 4
filename = input("Enter the mailbox file name: ")
try:
    mailbox = open(filename,'r')
except:
    print("file not found:",filename)
    exit()

email_addresses = dict()
for line in mailbox:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        email_addresses[words[1]] = email_addresses.get(words[1],0) + 1

print(email_addresses)

big_address = None
big_count = None
for k,v in email_addresses.items():
    if big_address is None or v > big_count:
        big_count = v
        big_address = k
print("")
print("More emails were received from",big_address,"than anyone else.")
print("They sent",big_count,"emails!")
