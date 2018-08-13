# Python for Everyone
# Chapter 12 exercise 4
# Create a program which uses urllib to
# 1)read data from a user specified url
# 2)count the number of paragraph tags
# 3)display the total number of paragraph tags
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

total = 0
tags = soup('p')
total = len(tags)

print('Total number of paragraph tags:',total)
