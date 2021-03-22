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
arrConn = []

def client_req(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected= True
    while(connected):
        msg_length = conn.recv(HEADER).decode(FORMAT) #Stop message
        if(msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg_array = msg.split(',')
            print(msg_array)
            print(f"[{addr}] {msg}")
            print("Connection: ", conn)
            if (msg_array[2] == "dst:Application"):
                print("Enviar mensaje a app")
            #conn.send("msg received".encode(FORMAT))
            conn.sendall("msg received".encode(FORMAT))
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
       # arrConn.append(add)      
        thread = threading.Thread(target=client_req, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

    
print("Server is starting")

start()

