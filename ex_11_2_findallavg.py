# Write a program to look for lines of the form: New Revision: 39772
import re
hand = open('mbox.txt') # mbox-short.txt # mbox.txt
l = list() # creating the list
i = 0 #creating a counter check
for line in hand: # using a regular expression and the findall() method.
    nums = re.findall('New Revision: ([0-9]+)', line) #find and extract all the numbers
    if len(nums) < 1 : continue # eliminate the lines that give no numbers
    for num in nums : # converting lists to numbers
        x = int(num)
        #print(x) #print check
        l.append(x) #list of numbers
        i = i + 1 #counter

#print(i)
#print(l)
# Compute the average of the numbers and print out the average as an integer.
avg = sum(l) / i
print(int(avg))

#there is also the option to do it with import statistics statistics.mean(l)
