def printHeader():
    print "Homework Assignment 4"
    print "September 27, 2010"
    print "CSE 1310-003"
    print "Richard Berry"
    print "ID# 1000739465"
    return

def problem4_33():
    titlestring="Melting and Boiling points of Alkanes" 
    r1c1string="Name"
    r1c2string="Melting Point (Deg C)"
    r1c3string="Boiling Point (Deg C)"
    r2c1string="Methane"
    r2c2string="-162"
    r2c3string="-183"
    r3c1string="Ethane"
    r3c2string="-48"
    r3c3string="-172"
    r4c1string="Propane"
    r4c2string="-42"
    r4c3string="-188"
    r5c1string="Butane"
    r5c2string="-0.5"
    r5c3string="-135"
    print '%s' %(titlestring.center(75))
    print '%s %s %s' %(r1c1string.ljust(25), r1c2string.ljust(26), r1c3string.ljust(52))
    print '%s %s %s' %(r2c1string.ljust(32), r2c2string.ljust(26), r2c3string.ljust(52))
    print '%s %s %s' %(r3c1string.ljust(32), r3c2string.ljust(26), r3c3string.ljust(52))
    print '%s %s %s' %(r4c1string.ljust(32), r4c2string.ljust(26), r4c3string.ljust(52))
    print '%s %s %s' %(r5c1string.ljust(32), r5c2string.ljust(26), r5c3string.ljust(52))
    return

def problem5_12():
    loop=True
    while (loop):
        option=raw_input("Please enter amount of money:")
        inputstring=option
        if (option=='5'):
            print "0 Extra Dollars..."
        elif (option=='10'):
            print "0 Extra Dollars..."
        elif (option=='25'):
            print "3 Extra Dollars..."
        elif (option=='50'):
            print "8 Extra Dollars..."
        elif (option=='100'):
            print "20 Extra Dollars..."
        elif (option=='q' or option=='Q'):
            loop=False
        else:
            print "%s is not valid." %(inputstring)
    return

def problem5_13():
    import math
    massString = raw_input("Enter the mass of your input:")
    massinteger = int(massString)
    speedlightString = "299792458"
    speedinteger = int(speedlightString)
    Energy = massinteger * speedinteger * speedinteger
    print "%s mkgs^2" %(Energy)
    return

#menu code
def menu():
    loop=True
    while (loop):
        print "-"*50
        print "1. Problem 4.33"
        print "2. Problem 5.12"
        print "3. Problem 5.13"
        print "Q. Quit"
        print "-"*50
        print " "
        option=raw_input("Please enter your selection:")
        if (option=='1'):
            problem4_33()
        elif (option=='2'):
            result=problem5_12()
        elif (option=='3'):
            result=problem5_13()
        elif (option=='q' or option=='Q'):
            loop=False
        else:
            print "Invalid Option"
            return
printHeader()
menu()