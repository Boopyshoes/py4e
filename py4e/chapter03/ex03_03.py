# Python for Everyone
# Chapter 3 exercise 3
try:
    score = float(input('Enter score: '))
except:
    score = -1

if score < 0.0  or score > 1.0:
    print('Bad Score:\n','  Score must be a number between 0.0 and 1.0')
else:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score > 0.6:
        print("D")
    else:
        print("F")
