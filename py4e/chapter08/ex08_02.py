# Python for Everyone: Chapter 8
# Exercise 2
filename = input('Enter file name: ')
try:
    fhand = open(filename)
except:
    print('File not found:',filename)
    exit()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    # this next if is the problem, because if a line has < 3 words and starts with From it's traceback time
    # if len(words) == 0:
    # corrected if looks like this
    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
    