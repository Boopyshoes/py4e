# Python for Everyone
# Chapter 4 exercise 7
def computegrade(score):
    if score < 0.0  or score > 1.0:
        return 'Bad Score:\n  Score must be a number between 0.0 and 1.0'
    else:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score > 0.6:
            return 'D'
        else:
            return 'F'
try:
    score = float(input('Enter score: '))
except:
    score = -1

print(computegrade(score))
