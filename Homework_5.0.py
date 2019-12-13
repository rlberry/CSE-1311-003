def printHeader():
    print "Homework Assignment 4"
    print "September 27, 2010"
    print "CSE 1310-003"
    print "Richard Berry"
    print "ID# 1000739465"
    return

def problem2_1():  #NOT COMPLETE
    import math
    divislist=[]
    for number in range(100,1000):
        if number % 17 == 0:
            divislist.append(number)
        else:
            continue
    print divislist

def problem2_2a(): #COMPLETE
    numStr = raw_input("enter number: ")
    num = int(numStr)
    sumlist=[]
    for number in range(1,num + 1,1):
        sumlist.append(number)
    print sum(sumlist)

def problem2_2b(): #---COMPLETE---
    import math
    numStr = raw_input("enter number: ")
    num = int(numStr)
    nMax = num#input number, convert to integer, change to nMax
    n = 1
    sumlist=[]
    while n <= nMax: 
        sum1n = 0
        i = 1
        while i <= n: #while n is less than nMax, add 1 to n, convert to i. add i +1 so that numbers add on each other. 
            sum1n += i
            i += 1
        sumlist.append(sum1n)
        n += 1
    print sumlist

def problem2_2c():  #--NOT STARTED--
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


def problem2_12():  #--NOT STARTED--
    print "alphabetical"
    alphaString = "alphabetical"
    alphaString
    'alphabetical'
    for theChar in "alphabetical":#print every third letter after the second letter => thus equaling pbil.
        print alphaString[2::3]
        break
    
#def pascalstriangle():  #--NOT STARTED--
 #   break

def menu():
    loop=True
    while (loop):
        print "-"*50
        print "1. Problem 2.1 Refactored"
        print "2. Problem 2.2a Refactored"
        print "3. Problem 2.2b Refactored"
        print "4. Problem 2.2c Refactored"
        print "5. Problem 2.12 Refactored"
        print "6. Pascals Triangle"
        print "Q. Quit"
        print "-"*50
        print " "
        option=raw_input("Please enter your selection:")
        if (option=='1'):
            problem2_1()
        elif (option=='2'):
            result=problem2_2a()
        elif (option=='3'):
            result=problem2_2b()
        elif (option=='4'):
            result=problem2_2c()
        elif (option=='5'):
            result=problem2_12()
        elif (option=='6'):
            result=pascalstriangle()
        elif (option=='q' or option=='Q'):
            loop=False
        else:
            print "Invalid Option"
            return
printHeader()
menu()    