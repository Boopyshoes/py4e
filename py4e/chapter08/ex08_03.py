# Python for Everyone
# Chapter 8 exercise 3
filename = input('Enter file name: ')
try:
    fhand = open(filename)
except:
    print('File not found:',filename)
    exit()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) >= 3 and words[0] == 'From':
        print(words[2])
