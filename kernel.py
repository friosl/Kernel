import os
from os import sys
import socket 
import threading 
import os
import os.path

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
        #try:
                   
        msg_length = conn.recv(HEADER).decode(FORMAT) #Stop message
        msg2 = msg_length[0:1]    
        if(msg_length):
            """
            if  msg2 == 0x00:
                print("Which one is ? 1")          
                connected=False                 
            """
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
        """
        if not gui:
            os.system('python gui.py')
            gui=True  
        """    
        conn, addr = server.accept()      
        thread = threading.Thread(target=client_req, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

    
print("Server is starting")

start()

