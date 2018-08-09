# Python for Everyone: Chapter 8
# Exercise 1
def chop(a_list):
    if len(a_list) >= 2:
        del a_list[0]
        a_list.pop()
    elif len(a_list) == 1:
        a_list.pop()
    else:
        pass

def middle(a_list):
    if len(a_list) >= 2:
        return a_list[1:-1]
    else:
        return []

colors = ['red','yellow','blue']
print(middle(colors))
print(colors)
chop(colors)
print(colors)

print(middle(colors))
print(colors)
chop(colors)
print(colors)

