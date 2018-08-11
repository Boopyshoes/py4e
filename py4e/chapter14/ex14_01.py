# Python for Everyone
# Chapter 14 Coursera Assignment 1 (week 5)
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url: ')
print('Retrieving', url)
xml_file = urllib.request.urlopen(url)
xml_data = xml_file.read()
print('Retrieved', len(xml_data), 'characters')
print(xml_data.decode())
tree = ET.fromstring(xml_data)

count = 0
total = 0
results = tree.findall('*//count')

for result in results:
    count += 1
    total += int(result.text)
   # print('<' + result.tag + '>' + result.text + '</' + result.tag + '>')

print('Count:',count)
print('Total:',total)