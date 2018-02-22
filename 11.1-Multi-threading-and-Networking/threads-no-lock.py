#!/bin/python

import threading
import time

class NewThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print("Starting {}".format(self.threadName))
        getTime(self.threadName)
        print("Exiting {}".format(self.threadName))

def getTime(threadName):
    count=10
    while count:
        time.sleep(1)
        print("{}: {}".format(threadName, time.ctime()))
        count -=1

def createThreads():
    thread1=NewThread("Thread-1")
    thread2=NewThread("Thread-2")
    thread3=NewThread("Thread-3")
    thread4=NewThread("Thread-4")
    return [thread1, thread2, thread3, thread4]

def startThreads(threads):
    for thread in threads:
        thread.start()

threads=createThreads()
startThreads(threads)

while len(threading.enumerate()) > 1:
    print("{} threads are still running...".format(len(threading.enumerate())))
    time.sleep(1)
    #pass

print("Exiting main thread")
