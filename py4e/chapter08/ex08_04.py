# Python for Everyone
# Chapter 8 exercise 4
filename = input('Enter file name: ')
try:
    fhand = open(filename)
except:
    print('File not found:',filename)
    exit()

word_list = []
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    for word in words:
        if word not in word_list:
            word_list.append(word)

word_list.sort()
print(word_list)
