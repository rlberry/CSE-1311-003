def problem1 ():
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
problem1()