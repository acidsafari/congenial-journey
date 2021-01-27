hrs = input("Enter Hours:") #employee input

try :
    h = float(hrs)#converting input to a number, assuming number only input
except :
    print('Please enter a numerical value')

hrate = input("Enter Rate:")
try :
    r = float(hrate)
except :
    print('Please enter a numerical value')

if h <= 40 : #if statement to account for the overtime variation
    p = h * r
else :
    p = (40 * r) + ((h - 40) * r * 1.5)

def computepay(h,r):
    print("Pay",p)
    return p

computepay(h,r)
