def problem5_13():
    import math
    massString = raw_input("Enter the mass of your input:")
    massinteger = int(massString)
    speedlightString = "299792458"
    speedinteger = int(speedlightString)
    Energy = massinteger * speedinteger * speedinteger
    print "%s mkgs^2" %(Energy)
    return
problem5_13()