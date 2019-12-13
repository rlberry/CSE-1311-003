import math

numStr = raw_input("enter number: ")
num = int(numStr)

theSum = num

for number in range(1,num,1):
    theSum = theSum + number
    
print "sum is:", theSum