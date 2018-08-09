hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
hrs = float(hrs)
rate = float(rate)

if hrs <= 40:
    # no overtime
    pay = rate * hrs
else:
    # calculate overtime
    pay = (hrs - 40) * rate * 1.5 + 40 * rate

print ("Pay:", pay)
