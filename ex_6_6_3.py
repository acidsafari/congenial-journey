word = input('Type word to count:')
letter = input('Type letter to count:')

def count (letter , word) :
    x = 0 #letter counter
    for l in word :
        if letter == l :
            x = x + 1
    print(x)

count(letter , word)
