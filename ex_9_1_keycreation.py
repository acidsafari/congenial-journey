fname = input("Enter file name: ") #open mbox-short.txt
if len(fname) < 1 : #new way to open only that file regardless
    fn = 'words.txt'

fw = open(fn)

newd = dict() #creating the dictionary
for lines in fw :
    words = lines.split()
    for word in words :
        newd[word] = ''

print(newd)
