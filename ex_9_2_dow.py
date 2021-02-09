fname = input('Enter File Name: ')
try:
    hand = open(fname)
except:
    print('Please Enter a CORRECT File Name:')
    exit()

ddow = dict()
#Write a program that categorizes each mail message by which day of the week
#the commit was done. To do this look for lines that start with “From”,
for line in hand :
    if not line.startswith('From ') : continue
    #print(line) checking for out of range error, due to 'From:' existing
    eh = line.split()
    dow = eh[2]
#then look for the third word and keep a running count of each of the days of the week.
    ddow[dow] = ddow.get(dow,0) + 1

#At the end of the program print out the contents of your dictionary (order does not matter).
print(ddow)
