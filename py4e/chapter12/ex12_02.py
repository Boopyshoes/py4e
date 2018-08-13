# Python for Everyone
# Chapter 12 exercise 2
# Create a program whichs
# 1)reads data from a user specified url
# 2)prints the first 3000 characters
# 3)displays the total number of characters
import socket

url = input('Enter the URL to download in the form http://www.example.com/somefile.ext\n')
url = url.rstrip()
domain = url.split('/')[2]
# print(domain)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((domain, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    # print(cmd)
    mysock.send(cmd)
except:
    print('Cannot open URL:',url)
    exit()

count = 0
while True:
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    count += len(data)
    if count <= 3000:
        print(data.decode(),end='')

print('downloaded:',count,'characters')
mysock.close()
