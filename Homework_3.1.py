def printHeader():
    print "Homework Assignment 2"
print "September 8, 2010"
print "CSE 1310-003"
print "Richard Berry"
print "ID# 1000739465"

printHeader()

loop=True
while (loop):
    print "--------------------------------------------------------------"
    print "1. Print out three-digit number divisible by 17"
    print "2. Print the sum of consectutive integers"
    print "3. Print the nested view of the sum of consecutive integers."
    print "4. Print the nested viwe of the sum of consectutive integers", \
      "only when the final sum is divisible by the number of operands."
    print "5. Print ''pbil'' from ''alphabetical''"
    print "Q. Quit"
    print "--------------------------------------------------------------"
    print " "
    option=raw_input("Please enter your selection:")
    if (option=='1'):
        print
        import math
        totalCount = 0
        for number in range(100,1000):
            if number % 17 == 0:
                print number
                totalCount = totalCount + 1
            else:
                continue
        print 'Total number of integers:', totalCount
        
    
    elif (option=='2'):
        print "Put your code for Problem 3.2a here"
    elif (option=='3'):
        print "Put your code for Problem 3.2b here"
    elif (option=='4'):
        print "Put your code for Problem 3.2c here"
    elif (option=='5'):
        print "Put your code for Problem 3.12 here"
    elif (option=='q' or option=='Q'):
        loop=False
    else:
        print "Invalid Option"
else:
    raw_input("Done")