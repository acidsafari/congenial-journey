# ----------------- WRITE -----------------
# we might have to create a new file to do this, or put it on the correct folder for use
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# can also use a for loop and a list
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open('Example2.txt', 'w') as writefile: #this writes over the one before
    for line in Lines:
        print(line)
        writefile.write(line)

with open('Example2.txt', 'w') as writefile: #i.e. of the OVERWRITE
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# ----------- APPENDING -----------------
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# WRITE and READ happen at certain location, 0 by default
with open('Example2.txt', 'a+') as testwritefile: # the a+ creates a new file if none exists
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

# here .tell() and .seek(offset,from) are use to position the reading and writting
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell())) # asking for the intial location

    data = testwritefile.read() # default for the read position is at the initial location
    if (not data):  #empty strings return false in python; which will be TRUE
            print('Read nothing') # if the initial location is at the end
    else:
            print(testwritefile.read())

    testwritefile.seek(0,0) # move 0 bytes from beginning. LIKE MOVING THE CURSOR TO THE START

    print("\nNew Location : {}".format(testwritefile.tell())) # here it will tell us the start
    data = testwritefile.read()                   # becuase we moved the cursor to the beginning
    if (not data):
            print('Read nothing')
    else:
            print(data)

    print("Location after read: {}".format(testwritefile.tell()) ) # and here it will be the end

# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file. deletes all and starts from the beginning!!!!!
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file, KEEPING WHAT WAS THERE

    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate() #deletes what was there and keeps the new written content
    testwritefile.seek(0,0)
    print(testwritefile.read())


# ------------------ COPY A FILE TO ANOTHER ----------------
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
