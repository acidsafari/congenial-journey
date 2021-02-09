name = input("Enter file name: ") #open mbox-short.txt
if len(name) < 1 : #new way to open only that file regardless
    name = "mbox-short.txt"

handle = open(name)
counts = dict()
#The program looks for 'From ' lines
for line in handle :
    if not line.startswith('From ') : continue #choose only the From lines
    hline = line.split()
        #if len(hline) == 0 or hline[0] != 'From ' : continue #safety check
#takes the second word of those lines as the person who sent the mail.
    email = hline[1]
#The program creates a Python dictionary that maps the sender's mail address
    counts[email] = counts.get(email,0) + 1

print(counts)
#to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
bigcount = None
bigword = None
for email,count in counts.items(): #finding the higher count ones
#using a maximum loop to find the most prolific committer.
    if bigcount is None or count > bigcount :
        bigword = email
        bigcount = count


print(bigword,bigcount)
