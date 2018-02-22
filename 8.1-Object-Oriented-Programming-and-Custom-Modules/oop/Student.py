#!/bin/python

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
student1 = Student('Joe Smith', '30')
student2 = Student('Pam Smith', '27')

print(student1.name, student1.age)
print(student2.name, student2.age)
