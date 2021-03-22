import os
from os import sys
import socket 
import threading 
import os
import os.path
import subprocess
import time

HEADER = 16
PORT = 5050
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
arrConn = []

"""kernel_send_app = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT_app = 5053
ADDR= (HOST,PORT_app)
kernel_send_app.connect(ADDR)
"""



def client_req(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT) #Stop message
        if(msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg_array = msg.split(',')
            target = msg_array[2]
            #print(msg_array)
            print(f"[{addr}] {msg}")
            #print(conn)
            if (target == "dst:Application"):
                #kernel_send_app.send(("open app").encode(FORMAT))
                #print("Enviar mensaje a app")
                conn = arrConn[2]
                # print(conn)
                print("antes de error")
                conn.send("Open app".encode(FORMAT))
                conn = arrConn[1]
                conn.send(msg_array[3].encode(FORMAT))
            elif (target == "dst:log"):
                print("Enviar mensaje a LOG")
                coon = arrConn[1]
                conn.send(msg_array[3].encode(FORMAT))
            elif (target == "dst:gui"):
                print("Enviar mensaje a GUI")
                coon = arrConn[1]

                conn.send(msg_array[3].encode(FORMAT))
            #conn.sendall("msg received".encode(FORMAT))   
        else:
            connected=False 
    conn.close()
    server.close()
    sys.exit()    

def start():
    server.listen()
    print(f"server is listenning on {HOST}")
    subprocess.call("start.bat")
    while True:
        conn, addr = server.accept()
        #print("address es: ")
        #print(addr[1])
        arrConn.append(conn)      
        thread = threading.Thread(target=client_req, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

    
print("Server is starting")

start()

