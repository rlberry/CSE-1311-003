import math
numStr = raw_input("enter number: ")
num= int(numStr)
nMax = num
n = 1
oplist=[]
sumlist=[]
while n <= nMax:#same as above...
    sum1n = 0
    i = 1
    while i <= n:
        sum1n += i
        i += 1
    n += 1
    if sum1n % nMax == 0:# if sum of nums is divisible by the number input, then print, else continue.
        sumlist.append(sum1n)
    else:
        continue
print oplist
print sumlist