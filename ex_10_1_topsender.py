#Revise a previous program 9_2_DOW as follows:
fname = input('Enter File Name: ')
try:
    hand = open(fname)
except:
    print('Please Enter a CORRECT File Name:')
    exit()

dsender = dict()
#Read and parse the “From” lines and pull out the addresses from the line.
for line in hand :
    if not line.startswith('From ') : continue #filtering lines
    #print(line) #checking for out of range error, due to 'From:' existing
    eh = line.split()
    s = eh[1] #picking the email address
#Count the number of messages from each person using a dictionary.
    dsender[s] = dsender.get(s,0) + 1

#print(dsender) #print check
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary.
lst = list() #creating a list of KEY, VAL TUPLES
for email, count in list(dsender.items()):
    lst.append((count, email))

#Then sort the list in reverse order and
lst.sort(reverse=True) #highest first.
#print(lst) #print check

#print out the person who has the most commits.
for key, val in lst[:1] :
    print(val, key)
