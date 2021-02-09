#more values than integers are valid for mapping
eng2sp = dict() #calling a dictionary
print(eng2sp)
#{} as a result
eng2sp['one'] = 'uno' #can add items like this
print(eng2sp)
#{'one': 'uno'}
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'} #keep in mind
#it works both ways, input and output
print(eng2sp)
#{'one': 'uno', 'three': 'tres', 'two': 'dos'} #also the order is randomised,
#although it feels like it is a .sort() output

vals = list(eng2sp.values()) #for values we need another function to check
'uno' in vals
#True

#Dictionary as a set of counters
word = 'brontosaurus'
d = dict()
for c in word: #effectively creating a histogram
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

print(d)

# using the method .get(key,defaultvalue) to COUNT
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1 #this is more concise loop with less lines

print(d)

#STRING METHODS TO CLEAN UP TEXT BEFORE PROCESSING 9.4
