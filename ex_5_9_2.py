largest = -1
smallest = None
while True :
    input_numbers = input("Enter Number: ") #employee input
    if input_numbers == 'done':#end condition before the loop in this case
        break
    try :
        num = int(input_numbers) #converting input to a number,
    except :
        print('Invalid input') #eliminating human error
        continue
    if num > largest :
        largest = num
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)
