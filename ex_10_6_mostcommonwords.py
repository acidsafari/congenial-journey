import string
fhand = open('romeo-full.txt')
counts = dict() #creating a dictionary with the words as KEYS
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    #    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words: #creating the counts as the VAL of the dictionary
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list() #creating a list of KEY, VAL TUPLES
for key, val in list(counts.items()):
    lst.append((val, key)) #but using the inverted VAL, KEY ORDER to be able to sort

lst.sort(reverse=True)

for key, val in lst[:10]: #printing only the top ten of the list 
    print(key, val)
