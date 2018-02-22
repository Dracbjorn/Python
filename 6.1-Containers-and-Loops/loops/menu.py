#!/bin/python

#nmap -p 22 -sS 172.16.0.0/16
ipList = ['172.16.0.1', '172.16.0.5', '172.16.0.15']

num=0
for selection in ipList:
    num+=1
    print(str(num) + ". " + selection)
print("0. Quit") 

while True:
    userInput=int(raw_input("Select an IP to connect to: "))
    
    if userInput == 0:
        exit()
    elif (userInput >= len(ipList)) or (userInput < 0):
        print("Selection invalid")
        continue
    else:
        print("Connecting to..."+ ipList[userInput-1])
        break
    

