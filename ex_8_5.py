fname = input("Enter file name: ") #open mbox-short.txt
if len(fname) < 1 : #new way to open only that file regardless
    fname = "mbox-short.txt"

fh = open(fname)
count = 0 #setting the counter to 0
for line in fh :
    if not line.startswith('From ') : continue#choose only the From lines
    count = count + 1
    bl = line.split()
    print(bl[1])

print("There were", count, "lines in the file with From as the first word")
