# Python for Everyone
# Chapter 9 exercise 5
filename = input("Enter the mailbox file name: ")
try:
    mailbox = open(filename,'r')
except:
    print("file not found:",filename)
    exit()

email_domains = dict()
for line in mailbox:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        at_loc = words[1].find('@')
        domain = words[1][at_loc+1:]
        email_domains[domain] = email_domains.get(domain,0) + 1

print(email_domains)

big_domain = None
big_count = None
for k,v in email_domains.items():
    if big_domain is None or v > big_count:
        big_count = v
        big_domain = k
print("")
print("More emails were received from",big_domain,"than anywhere else.")
print("They sent",big_count,"emails!")
