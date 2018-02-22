#!/usr/bin/python

import Car as c

car1 = c.Car('black','Ford','F150',1776)
car2 = c.Car('red','Volkswagon','Beetle',3010)
car3 = c.Car('blue','Delorean','v1',1985)

def viewCar(car):
    print(car.getColor())
    print(car.getMake())
    print(car.getModel())
    print(car.getYear())
    print(car.getSpeed())
    print(car.engineOn)

def startCar(car):
    car.startEngine()

def stopCar(car):
    car.stopEngine()

def accelerate(car,mph):
    for i in range(mph):
        car.speedUp()

def decelerate(car,mph):
    for i in range(mph):
        car.slowDown()

carList = [car1,car2,car3]

for car in carList:
    print("=================================")
    print("Car properties: ")
    viewCar(car)
    print("Starting car...")
    startCar(car)
    print("Current speed: "+str(car.speed))
    print("Speeding up...")
    accelerate(car,60)
    print("Current speed: "+str(car.speed))
    print("Slowing down...")
    decelerate(car,60)
    print("Current speed: "+str(car.speed))
    print("Turning off engine...")
    stopCar(car)
    print("Car properties: ")
    viewCar(car)
    print("==================================")
