#!/usr/bin/python

a=668.5
b=334.25
c=a+b
d=c-a
e=b*d
f=d/b

g=(b*2)+a
print("g="+str(g))

print("a="+str(a))
print("b="+str(b))

if a == b:
    print("a == b")

elif a != b:
    print("a != b")

elif a > b:
    print("a > b")

elif a < b:
    print("a < b")

elif a >= b:
    print("a >= b")

elif a <= b:
    print("a <= b")

print('(g >a) and (g == (a*2))) or ((d < g) and (g == b*4)')

if ((g > a) and (g == (a*2))) or ((d < g) and (g == b*4)):
    print(True)
else:
    print(False)

