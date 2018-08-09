# Python for Everyone: Chapter 8
# Exercise 6
numbers = []
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done': break
    try:
        user_input = float(user_input)
        numbers.append(user_input)
    except:
        print('bad data, not a number')

print('Maximum:',max(numbers))
print('Minimum:',min(numbers))

        