# Python for Everyone
# Chapter 10 exercise 3
import string

filename = input('Enter the file name: ')
try:
    fhand = open(filename,'r')
except:
    print('file not found:',filename)
    exit()

letters = dict()
letter_count = 0
for line in fhand:
    line = line.translate(line.maketrans('','',string.punctuation + string.whitespace + string.digits))
    line = line.lower()
    for letter in line:
        if letter >= 'a' and letter <= 'z':
            letters[letter] = letters.get(letter, 0) + 1
            letter_count = letter_count + 1

letters_vk = list()
for k,v in sorted(letters.items()):
    letters_vk.append((v,k))
    print(str(round((v/letter_count)*100, 2)) + '%' ,k)

print('')
print('')

letters_vk.sort(reverse=True)
for v,k in letters_vk:
    print(str(round((v/letter_count)*100, 2)) + '%' ,k)

fhand.close()
