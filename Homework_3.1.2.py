import math

numStr = raw_input("enter number: ")
num = int(numStr)

nMax = num
n = 1
while n <= nMax:
    sum1n = 0
    i = 1
    while i <= n:
        sum1n += i
        i += 1
    print(sum1n)
    n += 1