#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib

import socket

win = tk.Tk()
a5 = PhotoImage(file="g1.png")
win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("Demo Ship Tkinter")
win.geometry("500x500+0+0")
win.resizable(width=True, height=True)
win.configure(bg='black')

g_value=0
x=0



counter = tk.IntVar()

def socketSend(modified):
    s = socket.socket()
    s.connect(('127.0.0.1',12345))
    print("Send: "+ str(modified))
    s.send(str(modified).encode());
    s.close()

def socketReceive():
    s = socket.socket()
    port = 12346
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()
    print("Socket Up and running with a connection from",addr)
    rcvdData = c.recv(1024).decode()
    print("S:",rcvdData)
    c.close()
    if rcvdData == "":
        return("None")
    return(int(rcvdData))

def updateRudder(response, event=None):
    if response != "None":
        counter.set(response)
        p1.set_value(int(response))



def sendCommand(modified, event=None):
    
    
    socketSend(modified)
    response = socketReceive()
    if response == "None":
        return(response)

    return(response)

def onClickInc(event=None):
    current = counter.get() + 1 
    print("Inc: "+ str(current))
    response = sendCommand(current)
    updateRudder(response)

def onClickDec(event=None):
    current = counter.get() - 1 
    print("Dec: "+ str(current))
    response = sendCommand(current)
    updateRudder(response)

tk.Button(win, text="Increase", command=onClickInc, fg="dark green", bg = "white").pack()
tk.Button(win, text="Decrease", command=onClickDec, fg="dark green", bg = "white").pack()
tk.Label(win, textvariable=counter).pack()

p1 = gaugelib.DrawGauge2(
    win,
    max_value=35.0,
    min_value=-35.0,
    size=200,
    bg_col='black',
    unit = "Rudder Angle",bg_sel = 2)
p1.pack()

g_value=0
p1.set_value(int(g_value))
    

mainloop()
