# Python for Everyone
# Chapter 4 exercise 6
def computepay (hours, rate):
    if hours <= 40:
        # no overtime
        pay = rate * hours
    else:
        # calculate overtime
        pay = (hours - 40) * rate * 1.5 + 40 * rate
    return pay


try:
    hrs = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("Please enter a number")
    quit()

print("Pay:", computepay(hrs, rate))
