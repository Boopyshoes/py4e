def count(word, letter):
    count = 0

    try:
        if len(word) == 0:
            return -1
    except:
        return -1

    for char in word:
        if char == letter:
            count = count + 1
    return count


print(count('Banana','a'))
print(count(4,'a'))
