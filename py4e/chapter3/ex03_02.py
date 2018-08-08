try:
    hrs = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("Please enter a number")
    quit()

if hrs <= 40:
    # no overtime
    pay = rate * hrs
else:
    # calculate overtime
    pay = (hrs - 40) * rate * 1.5 + 40 * rate
print("Pay:", pay)
