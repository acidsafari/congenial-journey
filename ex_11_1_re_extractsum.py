# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
import re
hand = open('regex_sum_1144064.txt')
l = list() # creating the list
i = 0 #creating a counter check
for line in hand:
    nums = re.findall('([0-9]+)', line) #find and extract all the numbers
    if len(nums) < 1 : continue # eliminate the lines that give no numbers
    for num in nums : # converting lists to numbers
        x = int(num)
        #print(x) #print check
        l.append(x) #list of numbers
        i = i + 1 #counter

#print(i)
#print(l)
print('There are ', i, ' values with a sum=', sum(l))
