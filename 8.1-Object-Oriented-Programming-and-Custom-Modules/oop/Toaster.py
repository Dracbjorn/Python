#!/bin/python

class Toaster:
    def __init__(self, color, toastingLevels, numberOfSlots):

        self.color = color
        self.toastingLevels = toastingLevels
        self.numberOfSlots = numberOfSlots
        
        self.currentlyToasting = False

    def toast(self):
        self.currentlyToasting = True
"""
toaster1 = Toaster("silver", 3, 4)
print("Toaster color is "+ toaster1.color)
print("Number of levels are " + str(toaster1.toastingLevels))
print("Number of slots is " + str(toaster1.numberOfSlots))

toaster1.toast()

if toaster1.currentlyToasting == True:
    print("Currently toasting...")
elif toaster1.currentlyToasting == False:
    print("Not toasting.")
"""
