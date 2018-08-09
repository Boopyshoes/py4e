count = 0
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    count = count + 1
    if count == 1:
        big = num
        small = num
    elif count > 1 and big < num:
        big = num
    elif count > 1 and small > num:
        small = num


print('Maximum is',big)
print('Minimum is',small)
