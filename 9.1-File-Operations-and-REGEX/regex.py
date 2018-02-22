#!/bin/python

import re

ipList = [
  '192.168.122.1', '192.1111.22.1', 
  '10.11.32.254', '172.16.15.14', 
  '192,168,1,1', '255.255.255255', 
  '10.301.256', '301.999.999.999',
  '0.168.0.1', '192.168.1.255',
  '10.11.1.0', '-1.168.0.1', '0.23.4.56',
  '192.168.0.0'
]

pattern = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

for ip in ipList:
    valid=False
    if re.match(pattern, ip):
        valid=True
        octets = ip.split('.')

        for i in octets:
            if (int(i) < 0) or (int(i) > 255):
                valid=False
  
        #if (int(octets[3]) == 255) or (int(octets[3]) == 0) or (int(octets[0]) == 0):
            #valid=False
    #else:
    #    valid=False
    
    if valid == True:
        print("{} is VALID".format(ip))
    else:
        print("{} is INVALID".format(ip))
