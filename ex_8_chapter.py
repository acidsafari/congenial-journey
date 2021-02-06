#LISTS AND THEIR RULES AND OPERATIONS

#THE IN OPERATOR
cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
#True
'Brie' in cheeses
#False

#TRAVERSING
for cheese in cheeses:
    print(cheese)
#in case you want to write and not only read like above
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

#NOTICE ALL METHODS ACTUALLY CHANGE THE LIST, as they are mutable
#there are some methods .append() .extend(anotherlist) .sort()
#.pop(index#) del listname(index# or range) .remove(particular item)

# calculating averages like on the other chapter, this time with a LISTS
numlist = list() #make an empty list before the loop starts
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)#though this list doesn't have a try/except for errors

average = sum(numlist) / len(numlist)
print('Average:', average)

# LIST AND STRINGS
s = 'spam'
t = list(s) #convert a string into a list
print(t)
#['s', 'p', 'a', 'm']

s = 'pining for the fjords'
t = s.split() #converting a sentence with .split(delimiter i.e. -)
print(t)
#['pining', 'for', 'the', 'fjords']
print(t[2])
#the

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
#['spam', 'spam', 'spam']

#.join(delimiter) the inverse of split

#example of .split in use
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
