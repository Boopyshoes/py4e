# Python for Everyone
# Chapter 10 exercise 1
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

address_list = list()
for k,v in email_addresses.items():
    address_list.append((v,k))

address_list.sort(reverse=True)
for address in address_list:
    print(address)

print(address_list[0][1],address_list[0][0])
