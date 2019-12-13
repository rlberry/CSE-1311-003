def printHeader():
    print "Homework Assignment 2"#indented to remove error
    print "September 8, 2010"
    print "CSE 1310-003"
    print "Richard Berry"
    print "ID# 1000739465"
    return
#return function causing error... removed.
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
        import math
        totalCount = 0
        for number in range(100,1000): #= 100-999
            if number % 17 == 0: #if num in range divided by 17 =0, print and add to final count
                print number
                totalCount = totalCount + 1
            else: #otherwise, continue
                continue
        print 'Total number of integers:', totalCount
    elif (option=='2'):
        import math
        numStr = raw_input("enter number: ")
        num = int(numStr)#convert input to integer
        theSum = num
        for number in range(1,num,1):#take number in range and add to number
            theSum = theSum + number
            print "sum is:", theSum
    elif (option=='3'):
        import math
        numStr = raw_input("enter number: ")
        num = int(numStr)
        nMax = num#input number, convert to integer, change to nMax
        n = 1
        while n <= nMax: 
            sum1n = 0
            i = 1
            while i <= n: #while n is less than nMax, add 1 to n, convert to i. add i +1 so that numbers add on each other. 
                sum1n += i
                i += 1
            print(sum1n)
            n += 1
    elif (option=='4'):
        import math
        numStr = raw_input("enter number: ")
        num= int(numStr)
        nMax = num
        n = 1
        while n <= nMax:#same as above...
            sum1n = 0
            i = 1
            while i <= n:
                sum1n += i
                i += 1
            n += 1
        if sum1n % nMax == 0:# if sum of nums is divisible by the number input, then print, else continue.
            print sum1n, 'is divisible by', num
        else:
            continue

    elif (option=='5'):
        print "alphabetical"
        alphaString = "alphabetical"
        alphaString
        'alphabetical'
        for theChar in "alphabetical":#print every third letter after the second letter => thus equaling pbil.
            print alphaString[2::3]
            break

    elif (option=='q' or option=='Q'):
        loop=False
    else:
        print "Invalid Option"
else:
    raw_input("Done")