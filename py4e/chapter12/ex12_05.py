# Python for Everyone
# Chapter 12 exercise 5
# Create a program whichs
# 1)reads data from a user specified url
# 2) prints the data after the header and following blank line
import socket
import re

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

counter = 0
while True:
    counter += 1
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    data = data.decode()
    if counter > 1:
        print(data,end='')
    else:
        data = re.findall('Content-Type: \S+\s+(\S.+)', data, re.DOTALL)
        print(data[0], end='')

mysock.close()
