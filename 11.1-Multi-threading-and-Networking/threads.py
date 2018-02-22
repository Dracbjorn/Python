#!/bin/python

import threading
import time

class NewThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print("Starting {}".format(self.threadName))
        count=3
        while count:
            threadLock.acquire()
            print("{}: {}".format(self.threadName, time.ctime()))
            threadLock.release()
            time.sleep(1)
            count -=1
        print("Exiting {}".format(self.threadName))

def createThreads(numThreads):
    threadList = []
    while numThreads > 0:
        threadList.append(NewThread("Thread-"+str(numThreads)))
        numThreads -= 1
    return threadList

def startThreads(threads):
    for thread in threads:
        thread.start()

threadLock=threading.Lock()

threads=createThreads(5)
startThreads(threads)

#while len(threading.enumerate()) > 1:
    #print("{} threads are still running...".format(len(threading.enumerate())))
#    time.sleep(1)

#print("Exiting main thread")
