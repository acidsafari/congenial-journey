count = 0
tot = 0
while True :
    input_numbers = input("Enter Number: ") #employee input
    if input_numbers == 'done':#end condition before the loop in this case
        print('Done')
        break
    try :
        num = int(input_numbers) #converting input to a number,
    except :
        print('Please enter a numerical value') #eliminating human error
        continue
    print(num)
    count = count + 1
    tot = tot + num

print(tot, count, (tot/count))
print('Total: ', tot)
print('Count: ', count)
print('Average: ',(tot/count))
