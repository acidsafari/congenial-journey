hrs = input("Enter Hours:") #employee input

h = float(hrs)#converting input to a number, assuming number only input

hrate = input("Enter Rate:")

rate = float(hrate)

if h <= 40 : #if statement to account for the overtime variation
    pay = h * rate
else :
    pay = (40 * rate) + ((h - 40) * rate * 1.5)

print(pay)
