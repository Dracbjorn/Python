#!/usr/bin/python

primeList=[]

for num1 in range(1,101):

    isPrime=True

    for num2 in range(1,101):

        if (num1 == num2) or (num2 == 1):
            continue
        elif (num1 % num2 == 0) or (num1 == 1):
            isPrime=False
            break

    if isPrime == True:
        primeList.append(num1)

print("Prime Numbers between 1-100 are: ")
for primeNumber in primeList:
    print(primeNumber)

print("There are "+str(len(primeList))+" prime numbers from 1-100") 

