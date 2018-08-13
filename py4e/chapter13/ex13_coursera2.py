# Python for Everyone
# Chapter 13 Coursera week 4 assignment 2

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# retrives and parses the html from url
# returns a tuple (url, contents) from the nth anchor tag where n = position
# returns None for bad parameters
def getNthLinkData(url,position):
    if type(position) is not int:
        try:
            position = int(position)
        except:
            print("invalid paramaters: position cannot be converted to type int")
            return None
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    return [tags[position-1].get('href',None), tags[position-1].contents[0]]

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter starting url: ')
position = input ('Position of link to follow: ')
times = int(input ('How many links do you want to follow: '))

while times > 0:
    response = getNthLinkData(url,position)
    if response is None: break
    url = response[0]
    print("Name:",response[1],"Times:",times)
    times -= 1
