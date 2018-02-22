#!/bin/python

a,b,c,d="global","","",""

print(a,b,c,d)

def function1():
    b="function1"
    print(a,b,c,d)
    def function2():
        c="function2"
        print(a,b,c,d)
        def function3():
            d="function3"
            print(a,b,c,d)
        function3()
        print(a,b,c,d)
    function2()
    print(a,b,c,d)
function1()
print(a,b,c,d)
