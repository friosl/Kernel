import os
from os import sys
import socket 
import threading 
import os
import os.path
import subprocess
import time

HEADER = 1024
PORT = 5050
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = {}
arrCon = []
appbool = False
guibool = False
logsbool = False

#---------------------------------- C L I E N T   R E Q U E S T  --------------------------------------
def client_req(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    global appbool, guibool, logsbool
    
    while True:
        msg = None
        try:
            msg=conn.recv(HEADER).decode(FORMAT)
        except:
            print("Error receiving")

        if appbool == False or guibool == False or logsbool== False:
            if msg.startswith("App") and appbool == False:
                appbool=True
                print("APP CONNECTED")
                connections["App"]= conn
            elif msg.startswith("Gui") and guibool== False:
                guibool=True
                print("GUI CONNECTED")
                connections["Gui"]= conn
            elif msg.startswith("Log") and logsbool==False:
                logsbool=True
                print("LOGS CONNECTED")
                connections["Log"]= conn
        else:
            msg_array = msg.split(',')
            print(msg_array)
            target = msg_array[2]
            if (target == "dst:Application"):
                destino=connections["App"]
                message = msg.encode(FORMAT) 
                destino.send(message)
            elif(target == "dst:log"):
                message = msg.encode(FORMAT)                 
                destino=connections["Log"]
                destino.send(message)
            elif(target=="dst:gui"):
                message = msg.encode(FORMAT) 
                destino=connections["Gui"]
                destino.send(message)        



#--------------------------------------- S T A R T -------------------------------
def start():
    server.listen()
    subprocess.call("start.bat")
    print(f"server is listenning on {HOST}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_req, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

    
print("Server is starting")
start()

