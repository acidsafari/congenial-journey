# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    line = line.rstrip()
    print(line.upper())

#this line below gave me an \n error, which required a rstrip to eliminate double Enter
#print(inp.upper())
