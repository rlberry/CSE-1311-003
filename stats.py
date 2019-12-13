import math

#input
def inputFunction():
    dataset=input("please enter set of numbers")
    return dataset#returns tuple

#min
def minFunction(dataSet):
    return min(dataSet)

#max
def maxFunction(dataSet):
    return max(dataSet)
    
#mean
def meanFunction(dataSet):
    total=sum(dataSet)
    count=len(dataSet)
    meanval=total*1.0/float(count)
    return meanval

#stdDev
def stdDev(dataSet):
    meanvalu=meanFunction(dataset)
    toatl=0
    for number in dataset:
        difference=meanval-number
        square=difference**2
        total=total+square
    variation=total/(len(dataset)-1)
    result=math.sqrt(variation)
    return result

#median
def medianFunction(dataSet):
    newSet=sorted(dataSet)
    count=len(newSet)
    middle=count/2
    result=newSet[middle]
    return result

#mode
def modeFunction(dataSet):
    listValues=[]
    listCounts=[]
    for number in dataset:
        if number in listValues:
            cindex=listValues,index(number)
            listCounts[cindex]=listCounts[cindex]=1        
        else:
            listValues.append(number)
            listCount.append(1)
    maxval=maxfunction(listCounts)
    maxindex=listCounts.index(maxval)
    result=listValues(maxindex)
    return result

#output
def outputFunction():
    print dataset
    print "Min : %3.2f"%minval
    print "Max : %3.2f"%maxval
    
#=================================================
inputval=inputFunction()
print inputval

minval=minFunction()
print minval

maxval=maxFunction()
print maxval
