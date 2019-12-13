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