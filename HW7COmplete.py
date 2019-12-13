#C:\Users\Richard\Desktop\case1.txt

import math

#==================================================== 
# Name: Header
# Parameters: NONE
# Returns: NONE
# Input from Keyboard: NONE
# Output to Screen: Prints header at top of document
#Description: Header code. 
#Known Errors: NONE
def printHeader():
    print "Homework Assignment 4"
    print "September 27, 2010"
    print "CSE 1310-003"
    print "Richard Berry"
    print "ID# 1000739465"
    return
#====================================================

#==================================================== 
# Name: OpenFile
# Parameters: NONE
# Returns: NONE
# Input from Keyboard: The full path of the document.
# Output to Screen: The list of items in the document.
#Description: Makes CSV document into list, and makes it a global variable.
#Known Errors: NONE
def myOpenFile():
    filename=raw_input("Input Filename (Note: Input full filepath):")
    file=open(filename,'r')
    myString=file.read()
    myStringList= myString.split(',')
    myIntegerList=[]
    file.close()
    for item in myStringList:
        num=int(item)
        myIntegerList.append(num)
    local_variable=myIntegerList
    global local_variable
    return
#====================================================

#==================================================== 
# Name: MeanFunction
# Parameters: local_variable
# Returns: NONE
# Input from Keyboard: NONE
# Output to Screen: The mean of all numbers in file.
#Description: 
#Known Errors: NONE
def meanFunction(local_variable):
    total=sum(local_variable)
    count=len(local_variable)
    mean=total*1.0/float(count)
    global mean
    return
#====================================================

#==================================================== 
# Name: 
# Parameters: 
# Returns: 
# Input from Keyboard: 
# Output to Screen: 
#Description: 
#Known Errors:
def stdevFunction(local_variable):
    total=0
    for number in local_variable:
        difference=mean - number
        square=difference**2
        total=total+square
        n=len(local_variable)-1
    variation=total/(n)
    stdval=math.sqrt(variation)
    global stdval
    return
#====================================================

#==================================================== 
# Name: 
# Parameters: 
# Returns: 
# Input from Keyboard: 
# Output to Screen: 
#Description: 
#Known Errors: <function chartdiv at 0x0000000002583518>
def chartdiv (local_variable):
    counter0=0
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    counter6=0
    counter7=0
    counter8=0
    counter9=0
    for number in (local_variable):
        if number < mean-2.0*stdval: #final?
            counter0 = counter0 + 1
            continue
        elif mean-2.0*stdval< number <=mean-1.5*stdval:
            counter1 = counter1 + 1
            continue
        elif mean-1.5*stdval< number <=mean-1.0*stdval:
            counter2 = counter2 + 1
            continue
        elif mean-1.0*stdval< number <=mean-0.5*stdval:
            counter3 = counter3 + 1
            continue
        elif mean-0.5*stdval< number <=mean-0.0*stdval:
            counter4 = counter4 + 1
            continue
        elif mean-0.0*stdval< number <=mean+0.5*stdval:
            counter5 = counter5 + 1
            continue
        elif mean+0.5*stdval< number <=mean+1.0*stdval:
            counter6 = counter6 + 1
            continue
        elif mean+1.0*stdval< number <=mean+1.5*stdval:
            counter7 = counter7 + 1
            continue
        elif mean+1.5*stdval< number <=mean+2.0*stdval:
            counter9 = counter8 + 1
            continue
        elif mean+2.0*stdval< number: 
            counter9 = counter9 + 1
            continue
        else:
            print "Done"
    print '%s   %s' %("Counter #", "Count")
    print '%s   %s' %("Counter 0", counter0)
    print '%s   %s' %("Counter 1", counter1)
    print '%s   %s' %("Counter 2", counter2)
    print '%s   %s' %("Counter 3", counter3)
    print '%s   %s' %("Counter 4", counter4)
    print '%s   %s' %("Counter 5", counter5)
    print '%s   %s' %("Counter 6", counter6)
    print '%s   %s' %("Counter 7", counter7)
    print '%s   %s' %("Counter 8", counter8)
    print '%s   %s' %("Counter 9", counter9)
    return "Done"
#====================================================

#==================================================== 
# Name: 
# Parameters: 
# Returns: 
# Input from Keyboard: 
# Output to Screen: 
#Description: 

def menu():
    loop=True
    while (loop):
        print "-"*50
        print "1. Open File"
        print "2. Mean"
        print "3. Standard Deviation"
        print "4. Chart"
        print "Q. Quit"
        print "-"*50
        print " "
        option=raw_input("Please enter your selection:")
        if (option=='1'):
            myOpenFile()
            print local_variable
        elif (option=='2'):
            myOpenFile()
            meanFunction(local_variable)
            print mean
        elif (option=='3'):
            myOpenFile()
            meanFunction(local_variable)
            stdevFunction(local_variable)
            print stdval
        elif (option=='4'):
            myOpenFile()
            meanFunction(local_variable)
            stdevFunction(local_variable)
            chartdiv(local_variable)
            print chartdiv
        elif (option=='q' or option=='Q'):
            loop=False
        else:
            print "Invalid Option"
    return

printHeader()
menu()