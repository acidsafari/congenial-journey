fname = input("Enter file name: ") #input the file name romeo.txt
fh = open(fname) #open the file
lst = []
#for each line, split the line into a list of words using
for line in fh :
    words = line.split()
#for each word, check if the word is already in a listn
    for word in words :
        if word in lst : continue
#if not, add it to the list
        lst.append(word)

#when the program completes, sort and print the results in alphabetical order
lst.sort()
print(lst)
