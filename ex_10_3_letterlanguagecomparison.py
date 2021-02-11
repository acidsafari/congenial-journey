#Write a program that reads a file and prints the letters in decreasing order of frequency
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

#Your program should convert all the input to lower case and only count the letters a-z
lcount = dict() #creating the dicitonary with the .get method
for line in fhand:
    #THIS IS FROM CHAPTER 9.4 --TO CLEAN THE STRING BEFORE PROCESSING --
    line = line.translate(line.maketrans('', '', string.punctuation))
    #Your program should not count spaces, digits, punctuation,
    #or anything other than the letters a-z
    line = line.lower()
    words = line.split()
    for word in words :
        for l in word :
            lcount[l] = lcount.get(l,0) + 1

#print(lcount) #print check
#prints the letters in decreasing order of frequency
lst = list() #creating a list of KEY, VAL TUPLES
for k, v in list(lcount.items()):
    lst.append((v, k)) #flipping the sorting to the count value

#Then sort the list in reverse order for DECREASING
lst.sort(reverse=True) #highest first.
#print(lst) #print check

#prints out the letters with their corresponding count.
for key, val in lst :
    print(val, key)

#Find text samples from several different languages and
#see how letter frequency varies between languages
