import socket
import os
from datetime import datetime
from datetime import date
from os import path

pid = os.getpid() #Process ID

HEADER = 16
PORT   = 5053
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname()) #Nombre e IP de ntro pc
ADDR = (HOST, PORT)
app_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
app_listen.bind(ADDR)
app_listen.listen(5) 

app_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5050
ADDR= (HOST,PORT)
app_send.connect(ADDR)
print("APPLICATION binded to port 5053 and host is the same, listening")

while True: 
    msg = app_listen.recv(HEADER).decode(FORMAT)  
    print(msg)