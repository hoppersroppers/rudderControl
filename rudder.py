import socket
import time

def socketSend(modified):
    time.sleep(.1)
    s = socket.socket()
    s.connect(('127.0.0.1',12346))
    s.send(modified.encode());
    s.close()

def socketReceive():
    s = socket.socket()
    port = 12345
    s.bind(('', port))
    s.listen(1)
    c, addr = s.accept()
    print("Socket Up and running with a connection from",addr)
    rcvdData = c.recv(1024).decode()
    print("S:",rcvdData)
    rudderData = turnRudder(rcvdData)
    socketSend(rudderData)
    c.close()

def turnRudder(rcvdData):
    if int(rcvdData) >= 35:
        rcvdData = "35"
    if int(rcvdData) <= -35:
        rcvdData = "-35"
    return(rcvdData)
while True:
    socketReceive()

