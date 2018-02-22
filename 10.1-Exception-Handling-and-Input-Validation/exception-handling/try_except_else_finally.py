#!/usr/bin/python

def doTry(val):
    try:
        4/int(val)
    except ValueError:
        print("ValueError: "+ str(ValueError))
    except ArithmeticError as err:
        print("ArithmeticError: " + str(err))
    except:
        print("Except: EXCEPTION!")
    else:
        print("Else: This executes if there's no exception")
    finally:
        print("Finally: This executes whether or not there's an exception")

doTry(0)
print("------------")
doTry("a")
print("------------")
doTry(2)
print("------------")

