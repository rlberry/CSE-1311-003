def printHeader():
    print "Homework Assignment 2"
print "September 8, 2010"
print "CSE 1310 003"
print "Richard Berry"
print "ID# 1000739465"
printHeader()
print
#ATTN: 
#Given Information:
#The Great Lakes contain 22,810 km3 of water
#The area of the 48 States is 3,119,884.69 square miles
#1 square mile is 2.59 square kilometers
#The depth of water should be given in inches, feet, and meters to receive full credit.
#You must show the calculations for finding each of these units of measurement.

import math #import math module

GLVolumeString = 22810 #create string with great lakes volume
ContUSAreaString = 3119884.69 #create string with cont us area
sqmileString = 2.59 #create string with sq mile to sq kilometer conversion

print "The great lakes contain 22810 cubic kilometers of water."
print "1 square mile = 2.59 square kilometers"
print "The continental us is 3119884.69 square miles."
print
#multiply contusstring by sqmilestring to get cont us area in kilometers
contusareakilo = ContUSAreaString * sqmileString

print "multiply the are of the continental US by 2.59"
print "which yields:"
print "the area of the continental us in kilometers is:"
print contusareakilo, "kilometers"
print
print "divide the area of the continental US in Kilometers by volume"
print "which yields"
#divide contusareakilo by glvolume for depth
depth = GLVolumeString / contusareakilo
print depth,"meters deep"
print
print "divide by 3.2808..."
depthfeet = depth / 3.28083989501

print depthfeet,"feet deep"
print
print "divide by 12..."
depthinches = depthfeet / 12

print depthinches,"inches deep"
print
print "In short, the volume of water in the great lakes would cover the continental united states to a depth of",depth,"meters or,",depthfeet,"feet or",depthinches,"inches."

raw_input("Done")