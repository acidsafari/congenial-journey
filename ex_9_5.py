name = input("Enter file name: ") #open mbox-short.txt
if len(name) < 1 : #new way to open only that file regardless
    name = "mbox-short.txt"

handle = open(name)
dom = dict()
#The program looks for 'From ' lines
for line in handle :
    if not line.startswith('From ') : continue #choose only the From lines
    id0 = line.find('@') #to pick the spot to cut
    arro = line[id0+1:] #the new lines starting from @+1
    arro = arro.split() #creating the list per line
    doms = arro[0] #picking the item of the list we are interested in
    dom[doms] = dom.get(doms,0) + 1 #creating the dictionary and counter

print(dom)
