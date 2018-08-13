# Python for Everyone
# Chapter 12 exercise 3
# Create a program which uses urllib to
# 1)read data from a user specified url
# 2)print the first 3000 characters
# 3)display the total number of characters
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url to read - ')

html = urlopen(url, context=ctx).read()
html = html.decode()
print(html[:3000])
total = len(html)
print('Total characters downloaded:',total)
