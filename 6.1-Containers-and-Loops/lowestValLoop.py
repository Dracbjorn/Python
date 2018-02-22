#!/usr/bin/python

def smallestNum(numberList):

    lowestValue=numberList[0]

    for number in numberList:
        
        print("Is {} less than {}?".format(number,lowestValue))
        if number < lowestValue:
            print("{} is less than {}".format(number,lowestValue))
            lowestValue=number
            print("{} is the new lowest value".format(lowestValue))

    print("The lowest value is: "+str(lowestValue))

smallestNum([9999,-999999,0,2,11,-23,-8,44,7,12,-1])

#numbers.sort()
#numbers[0]

#min(numbers)
