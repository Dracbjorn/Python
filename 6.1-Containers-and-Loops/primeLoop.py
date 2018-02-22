#!/usr/bin/python

primeList=[]

for num1 in range(2,101):

    isPrime=True

    print("Is {} a prime number?".format(num1))

    for num2 in range(2,101):
        
        if (num1 == num2):
            continue
        elif (num1 % num2 == 0):
            print("{} IS NOT PRIME:  {} is divisible by {}".format(num1,num1,num2))
            isPrime=False
            break

    if isPrime == True:
        print("{} IS PRIME".format(num1))
        primeList.append(num1)

print("Prime Numbers between 1-100 are: ")
for primeNumber in primeList:
    print(primeNumber)

print("There are "+str(len(primeList))+" prime numbers from 1-100") 

