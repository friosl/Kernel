import socket
import os
from datetime import datetime
from datetime import date
from os import path
import subprocess
from random import randrange
import time
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
    back_up_file = open("logs_backup.txt", 'a')
    back_up_file.write(msg+"\n")
    back_up_file.close()
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    messageArray= msg.split(",")
    print("MSG ARRAY:", messageArray)
    if(messageArray[0]=="status:BUSY" or messageArray[0]=="status:PROC"):
        
        if(messageArray[-1]=="OPEN APP"):
            subprocess.call("openApp.bat")

            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:log,msg:'\log: " + current_time + " "+ current_date+ ",OPEN APP"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)


        elif(messageArray[-1]=="CLOSE APP"):
            subprocess.call("closeApp.bat")  
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:log,msg:'\log: " + current_time + " "+ current_date + ",CLOSE APP"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)
    
    elif(messageArray[0]=="status:ERROR"):
        subprocess.call("closeApp.bat")
        print("CLOSE APPS BY ERROR....")

       