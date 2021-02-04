#OPENING FILES
fhand = open('filename.extension')
print(fhand)
# this is the result <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>

#COUNTING LINES
fhand = open('mbox-short.txt')
count = 0 #to count the lines
for line in fhand: #becuase it reads the file handle as a squence of lines
    count = count + 1

print('Line Count:', count)

#COUNT ITEMS
fhand = open('mbox-short.txt')
inp = fhand.read() #in this case it is reading the whole file as a string, even the \n
print(len(inp))
94626
print(inp[:20]) #to print the first 20 characters
# reult: From stephen.marquar

#SEARCHING IN A file
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'): #this one prints the new lines with \n
        print(line) #problem is that print adds \n bewteen them
        count = count + 1

print(count)

#PRINTING A SELECTION
fhand = open('mbox-short.txt')
x = 0
for line in fhand:
    line = line.rstrip() #this eliminates the \n at the end of the line in the file
    if line.startswith('From:'):
        print(line)
        x = x + 1

print(x)

#A DIFFERENT WAY OF PRINTING A SELECTION
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): # Skip 'uninteresting lines'
        continue #goes back to the top
    # Process our 'interesting' line
    #stylistically better to skip the unwanted and to let the good ones fall through
    print(line)

#USING FIND TO PERFORM A SIMILAR TASK THAN BEFORE
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:#Now we are looking for a different item
        continue
    print(line)
