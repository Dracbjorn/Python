#!/usr/bin/python

def smallestNum(numberList):

    lowestValue=99999999999999999

    for number in numberList:

        if number < lowestValue:
            lowestValue=number

    print("The lowest value is: "+str(lowestValue))

smallestNum([0,2,11,-23,-8,44,7,12,-1])
