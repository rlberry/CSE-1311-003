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
problem5_12()