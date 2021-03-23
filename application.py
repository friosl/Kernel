import socket
import os
from datetime import datetime
from datetime import date
from os import path
import subprocess

pid = os.getpid() #Process ID

HEADER = 1024
PORT   = 5050
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname()) #Nombre e IP de ntro pc

app_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR= (HOST,PORT)
app_send.connect(ADDR)
print("APPLICATION binded to port 5050 ")

msg="App"
app_send.send(msg.encode(FORMAT))

opened_processes = []

while True: 
    msg = app_send.recv(HEADER).decode(FORMAT)  
    print(msg)
    #back_up_file = open("logs_backup.txt", 'a')
    #back_up_file.write(msg+"\n")
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    messageArray= msg.split(",")
    print("MSG ARRAY:", messageArray)
    if(messageArray[-1]=="OPEN APP"):
        msg="cmd:send,src:Application,dst:log,msg:'\log: " + current_time + " "+ current_date+ ",OPEN APP"
        msg_send=msg.encode(FORMAT)
        app_send.send(msg_send)
        subprocess.call("openApp.bat")
        print("Abrí el programa")
    elif(messageArray[-1]=="CLOSE APP"):
        print("Entré")
        msg="cmd:send,src:Application,dst:log,msg:'\log: " + current_time + " "+ current_date + ",CLOSE APP"
        msg_send=msg.encode(FORMAT)
        app_send.send(msg_send)
        subprocess.call("closeApp.bat")       