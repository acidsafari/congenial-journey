#Write a program to read through the mbox-short.txt
name = input("Enter file name: ") #open mbox-short.txt
if len(name) < 1 : #new way to open only that file regardless
    name = "mbox-short.txt"

handle = open(name)
#figure out who has sent the greatest number of mail messages.
counts = dict() #creating the dicitonary with the .get method
#The program looks for 'From ' lines
for line in handle :
    #line = line.rstrip() #it doesnt make a different with the factor of 7 I am getting
    if not line.startswith('From ') : continue #choose only the From lines
    hline = line.split()
        #if len(hline) == 0 or hline[0] != 'From ' : continue #safety check
#takes the second word of those lines as the person who sent the mail.
    #print(hline)
    #email = print(hline[1])
    email = hline[1]
#The program creates a Python dictionary that maps the sender's mail address
    counts[email] = counts.get(email,0) + 1

print(counts)
