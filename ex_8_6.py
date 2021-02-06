numlist = list() #make an empty list before the loop starts
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)#though this list doesn't have a try/except for errors

print('Maximum: ', max(numlist))
print('Minimum: ', min(numlist))
