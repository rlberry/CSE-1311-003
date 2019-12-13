import math

totalCount = 0
for number in range(100,1000):
    if number % 17 == 0:
        print number
        totalCount = totalCount + 1
    else:
        continue

print 'Total number of integers:', totalCount

    