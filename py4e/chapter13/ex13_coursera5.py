# Python for Everyone
# Chapter 13 Coursera Week 6 Assignment 1
import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter url: ')
print('Retrieving', url)
json_file = urllib.request.urlopen(url)
json_data = json_file.read()
print('Retrieved', len(json_data), 'characters')

info = json.loads(json_data)
print('User count:', len(info))
count = 0
print(json.dumps(info, indent=4))
for comment in info["comments"]:
    count += int(comment['count'])

print('Total:',count)
