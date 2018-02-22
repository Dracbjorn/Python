#!/usr/bin/python
import sys

x=int(sys.argv[1])
y=int(sys.argv[2])

def subtraction(num1, num2):
    return num1 - num2

def divisible(num):

    isEven=num%2

    if isEven == 0:

        difference=subtraction(num,1000)

        return difference

    else:
        
        return num

def multiply(num1, num2):

    return num1*num2

def addition(a):
    
    b=multiply(672.5,2.0)
    
    return a + b

num1=divisible(x)
num2=divisible(y)

product=multiply(num1,num2)

result=addition(product)

print(result)
print(type(result))
