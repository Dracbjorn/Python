#!/bin/python

import sys

x = sys.argv[1]
y = sys.argv[2]

def subtraction(num1, num2):
    return num1 - num2

def divisible(num):
    if (num % 2) == 0:
        return subtraction(num, 1000)
    else:
        return num

def multiply(num1, num2):
    return num1 * num2

def addition(a):
    b = 672.5 * 2
    return a + b

print(addition( multiply( divisible(x), divisible(y) ) ) )

