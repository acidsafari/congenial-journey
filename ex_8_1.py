#write a function called chop that modifies lists
def chop(t) :
    del t[0] #deletes the first place
    del t[-1] #deletes the last place
    return None

#write a funciton called middle that contains all but the 1st and the last
def middle(t) :
    new = t[1:] #new list without the first item
    del new[-1]
    return new


hola = ['h','o','l','a']
hcc = ['H','O','L','A']

nicht = chop(hola)
print(hola)
print(nicht)
print(['after chop: ', print(hola), print(nicht)])

ol = middle(hcc)
print(hcc)
print(ol)
print(['after middle: ', print(hcc), print(ol)])


print(['check changes', print(hola), print(hcc), 'think about that'])
