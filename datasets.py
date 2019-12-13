import math


def inputFunction():
    dataset=input("Please enter a set of numbers:")
    return dataset

def maxFunction(dataSet):
    return max(dataSet)


def minFunction(dataSet):
    return min(dataSet)

def meanFunction(dataSet):
    total=sum(dataSet)
    count=len(dataSet)
    mean=total*1.0/float(count)
    return mean

def stdevFunction(dataset):
    meanval=meanFunction(dataset)
    total=0
    for number in dataset:
        difference=meanval-number
        square=difference**2
        total=total+square
    
        n=len(dataset)-1
    variation=total/(n)
    
    result=math.sqrt(variation)
    return result
    
def medianFunction(dataset):
    newset=sorted(dataset)
    count=len(newset)
    middle=count/2
    result=newset[middle]
    return result

def modeFunction(dataset):
    listValues=[]
    listCounts=[]

    for number in dataset:
        if number in listValues:
            cindex=listValues.index(number)
            listCounts[cindex]=listCounts[cindex]+1
        else:
            listValues.append(number)
            listCounts.append(1)
    
    maxval=maxFunction(listCounts)
    maxindex=listCounts.index(maxval)
    result=listValues[maxindex]
    return result

def outputFunction (dataset,minval,maxval,meanval,medianval,modeval,stdVal):
    print dataset
    print "Min   : %3.2f"%minval
    print "Max   : %3.2f"%maxval
    print "Mean  : %3.2f"%meanval
    print "Median: %3.2f"%medianval
    print "Mode  : %3.2f"%modeval
    print "Stdev : %3.2f"% stdVal


dataset=inputFunction()
print dataset

minval=minFunction(dataset)
print minval

maxval=maxFunction(dataset)
print maxval

meanval=meanFunction(dataset)
print meanval


stdVal=stdevFunction(dataset)
print stdVal

medianval=medianFunction(dataset)
print medianval

modeval=modeFunction(dataset)
print modeval

outputFunction (dataset,minval,maxval,meanval,medianval,modeval,stdVal)