#!/usr/bin/python

exercise="global"
print(exercise)

def function1():
    exercise="local"
    print(exercise)

    def function2():
        exercise="local2"
        print(exercise)
    
    function2()
    
    return exercise

function1()

print(exercise)



