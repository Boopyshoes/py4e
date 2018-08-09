# Python for Everyone
# Chapter 5 exercise 1
total = 0
count = 0

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('bad data')
        continue
    total = total + num
    count = count + 1

print('The total is:',total)
print('The count is:',count)
print('The average is"',total / count)
