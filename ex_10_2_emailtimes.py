name = input("Enter file name: ")
if len(name) < 1 : #open only that file regardless
    name = "mbox-short.txt" #open mbox-short.txt

handle = open(name)
#figure out the distribution by hour of the day for each of the messages.
counts = dict() #creating the dicitonary with the .get method
for line in handle :#The program looks for 'From ' lines
    if not line.startswith('From ') : continue #choose only the From lines
    hline = line.split()
        #if len(hline) == 0 or hline[0] != 'From ' : continue #safety check
#You can pull the hour out from the 'From ' line
    #print(hline) #check
    fhour = hline[5]
    fhour.split(':')
    hour = fhour[:2] #when putting the int() here, it looses the 0s at the front
#by finding the time and then splitting the string a second time using a colon.
    counts[hour] = counts.get(hour,0) + 1

#print(counts) #print check
#Once you have accumulated the counts for each hour,
lst = list() #creating a list of KEY, VAL TUPLES
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort() #print out the counts, sorted by hour as shown below.

for key, val in lst :
    print(key, val)

#print(lst) #print check
