#!/usr/bin/python

def sing(numBeers):
    print(str(numBeers)+" bottles of beer on the wall, " +\
          str(numBeers)+" bottles of beer!")
    if numBeers == 0:
        return
    print("Take one down, pass it around. "+str(numBeers-1) +\
          " bottles of beer on the wall!") 

#numBeers=99
#while numBeers >= 0:
#    sing(numBeers)
#    numBeers -= 1

for numBeers in reversed(range(100)):
    sing(numBeers)

#for numBeers in range(99,-1,-1):
#    sing(numBeers)
