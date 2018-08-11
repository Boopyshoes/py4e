# Python for Everyone
# Chapter 13 Coursera Assignment 1

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url to read - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0
tags = soup('span')
for tag in tags:
    total += int(tag.contents[0])
    count += 1

print('Total:',total)
print('Count',count)