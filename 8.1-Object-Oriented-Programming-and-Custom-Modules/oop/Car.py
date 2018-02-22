class Car:
    def __init__(self,color,make,model,year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.engineOn = False
        self.speed = 0

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getSpeed(self):
        return self.speed

    def startEngine(self):
        self.engineOn = True

    def stopEngine(self):
        self.engineOn = False

    def speedUp(self):
        self.speed += 1

    def slowDown(self):
        self.speed -= 1
