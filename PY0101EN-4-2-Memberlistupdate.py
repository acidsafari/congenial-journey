'''
Your local university's Raptors fan club maintains a register of its active members on a .txt doc
Every month they update the file by removing the members who are not active.
You have been tasked with automating this with your python skills.
Given the file currentMem, Remove each member with a 'no' in their inactive coloumn.
Keep track of each of the removed members and append them to the exMem file.
Make sure the format of the original files in preserved.
(Hint: Do this by reading/writing whole lines and ensuring the header remains )
Run the code block below prior to starting the exercise.
The skeleton code has been provided for you, Edit only the cleanFiles function.

Run this prior to starting the exercise
'''
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: # creating the new lists
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(20): #running only a sample batch
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))

    with open(old,'w+') as writefile: # creating the old lists
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3): #another sample of 3 from the list
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

genFiles(memReg,exReg)

# Start your solution below:

def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: # so that it doesn't delete the data r+
        with open(exMem,'a+') as appendFile: # to add the new values to the old list a+
            #get the data
            writeFile.seek(0) #start from the beginning
            members = writeFile.readlines() #read the lines
            #remove header
            header = members[0]
            members.pop(0)
#the innactive list, cool way to code
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as

            for member in active:
            if 'no' in member:
                inactive.append(member)
            '''
            #go to the beginning of the write file
            writeFile.seek(0) # which is the a new version of currentMem
            writeFile.write(header) # write the old header
            for member in members: #sorting the members in two lists
                if (member in inactive):
                    appendFile.write(member) #this is the new exMem
                else:
                    writeFile.write(member)
            writeFile.truncate() #eliminate the old old values


# Code to help you see the files
# Leave as is
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

# Result
'''
Active Members:


Membership No  Date Joined  Active
    75518      2015-12-5    yes
    73888      2015-7-2     yes
    57196      2020-10-16   yes
    27073      2017-10-14   yes
    75956      2017-8-6     yes
    43362      2018-11-20   yes
    95171      2015-8-10    yes
    14592      2017-6-20    yes
    13235      2017-2-2     yes

Inactive Members:


Membership No  Date Joined  Active
    64394      2019-2-3     no
    40278      2018-9-17    no
    64155      2019-6-21    no
    81540      2017-4-21    no
    97862      2016-2-3     no
    82294      2018-2-6     no
    64651      2017-12-20   no
    72808      2016-12-20   no
    64391      2017-5-5     no
    42559      2016-10-10   no
    38288      2018-7-1     no
    94502      2018-3-5     no
    81969      2018-9-17    no
    88948      2018-9-6     no
'''
# test code
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt"
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()

# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False

for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
