# FUNCTIONS EXERCISE
# You have been tasked with creating a lab that demonstrates the basics of probability
# by simulating a bag filled with colored balls.
# The bag is represented using a dictionary called "bag",
# where the key represents the color of the ball and the value represents the no of balls.
#CREATE A NUMBER OF FUNCTIONS
# fillBag - A function that packs it's arguments into a global dictionary "bag"
def fillBag(**balls): #function to fill the bag DONT FORGET TO ADD THE ** WHEN UNPACKING
    global bag #creating the bag
    bag = balls #calling the elements on the bag
    return bag

# totalBalls - returns the total no of balls in the bucket
def totalBalls(x):
    return sum(x.values())

# probOf - takes a color (string) as argument and
#returns probability of drawing the selected ball.
def probOf(color):
    prob1ballDict = {}
    for color in bag :
        prob1ballDict[color] = round((bag[color]/totalBalls(bag))*(1/totalBalls(bag)),5)
        #compound probability
    return prob1ballDict  # list of the probabilities by color


def probAll(color):
    probDict = {}
    for color in bag :
        probDict[color] = round(bag[color]/totalBalls(bag) , 5)
    return probDict

# THIS WORKS
testBag = dict(red = 12, blue = 20, green = 14, grey = 10)

bag = fillBag(**testBag) #IT NEEDS TO BE DONE THIS WAY trial and error
print(bag)
total = totalBalls(bag)
print('the bag has ',total, 'balls in total')
print('Dictionary of the probabilities per ball:', probOf(bag))
print('Dictionary of the probabilities per color: ' , probAll(bag))

# -------------------------- GOOD AS AN EXAMPLE --------------------------
# THIS IS A TRY AND EXCEPT BLOCK THEY PROVIDED
# which I had to tweak too in order to make it work
testBag = dict(red = 12, blue = 20, green = 14, grey = 10)
total =  sum(testBag.values())
prob={}
for color in testBag:
    prob[color] = testBag[color]/total;

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("fillBag : ")
try:
    fillBag(**testBag)
    print(testMsg(bag == testBag))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")

print("totalBalls : ")
try:
    print(testMsg(total == totalBalls(bag)))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")

# THIS SECTION OF THE TRY-EXCEPT BLOCK WON'T WORK
print("probOf") #this I won't get right, becuase the correct equation they asked for, is not the simple
try:    # solution the provided, so the conditional values won't match
    passed = True
    for color in testBag:
           if probOf(color) != prob[color]:
                passed = False

    print(testMsg(passed) )
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")

print("probAll")
try:
    print(testMsg(probAll() == prob))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
