import math

numStr = raw_input("enter number: ")
num= int(numStr)

nMax = num
n = 1
while n <= nMax:
    sum1n = 0
    i = 1
    while i <= n:
        sum1n += i
        i += 1
    n += 1
    if sum1n % nMax == 0:
        print sum1n, 'is divisible by', num
    
    else:
        continue
