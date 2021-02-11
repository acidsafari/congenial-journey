#TUPLES
t = tuple()
print(t)
#()

t = tuple('lupins')
print(t)
#('l', 'u', 'p', 'i', 'n', 's') can do parsin

t[0] = 'A'
#TypeError: object doesn't support item assignment
#can't do modifying, but CAN REPLACE TUPLE WITH ANOTHER
t = ('A',) + t[1:]
print(t)
#('A', 'b', 'c', 'd', 'e')

#EXAMPLE OF TUPLE USE IN ODER TO MAKE A LIST
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word)) #this creates a list of tuples

#print(t) to check the tuple created
t.sort(reverse=True) #sorts the list in decreasing order
res = list()
for length, word in t: #conditon for the tuples
    res.append(word)

print(res)

#TUPLE ASSIGNMENT
m = [ 'have', 'fun' ]
x, y = m
x
#'have'
y
#'fun'

#Application of the assignment
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
#monty
print(domain)
#python.org

# .items() method TO CREATE A LIST of tuples
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
#[('b', 1), ('a', 10), ('c', 22)]

#this way we can SWAP KEY, VAL POSITIONS for different uses
for key, val in list(d.items()):
    print(val, key)

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
    l.append( (val, key) ) #creating a list with VAL, KEY
print(l)
#[(10, 'a'), (22, 'c'), (1, 'b')]
l.sort(reverse=True) #sorting it with the values in reverse
print(l)
[(22, 'c'), (10, 'a'), (1, 'b')]

#PHONE BOOK EXAMPLE
directory[last,first] = number
for last, first in directory:
    print(first, last, directory[last,first])
