# Python for Everyone
# Chapter 12 exercise 1
# Create an improved version of socket1.py
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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
