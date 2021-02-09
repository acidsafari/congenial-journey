import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict() #creating the dicitonary with the .get method
for line in fhand:
    #THIS IS FROM CHAPTER 9.4 --TO CLEAN THE STRING BEFORE PROCESSING --
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): #finding the higher count ones
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(counts)
