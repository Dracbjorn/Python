#!/bin/python
import sys

while True:
    try:
        int1 = int(raw_input("Enter first integer value between 1 and 100: "))
        int2 = int(raw_input("Enter second integer value between 1 and 100: "))
        if (int1 <= 100) and (int1 >= 1) and (int2 <= 100) and (int2 >= 1):
            print("{} * {} = {}".format(int1,int2,(int1*int2)))
            for i in int1, int2:
                try:
                    print("{} / 0 = {}".format(i,(i/0)))
                except ZeroDivisionError:
                    print("You cannot divide by zero!")
                    continue
    except ValueError:
        print("ERROR: Please enter an integer value!")
        continue
    except KeyboardInterrupt:
        print('\nExiting...')
        sys.exit()
