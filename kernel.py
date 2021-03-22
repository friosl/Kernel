import os
from os import sys
import socket 
import threading 
import os
import os.path

import time

HEADER = 16
PORT = 5050
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def client_req(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected= True
    while(connected):
        msg_length = conn.recv(HEADER).decode(FORMAT) #Stop message
        msg2 = msg_length[0:1]    
        if(msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            conn.send("msg received".encode(FORMAT))
        else:
            connected=False 
    conn.close()
    server.close()
    sys.exit()    

def start():
    server.listen()
    print(f"server is listenning on {SERVER}")
    gui= False
    while True:
        conn, addr = server.accept()      
        thread = threading.Thread(target=client_req, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

    
print("Server is starting")

start()

