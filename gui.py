import socket
import os

from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(800,800)
#show_about()
#show_documentation()
pid = os.getpid() #Process ID

HEADER = 16
PORT   = 5050
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname()) #Nombre e IP de ntro pc
ADDR   = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(pid) #Pasar este PID por sockets al kernel
#Meter esto de abajo dentro de un método
def sendPID():
    message = str(pid).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length)) #Adding blankspaces
    client.send(send_length)
    client.send(message) 
    print(client.recv(2048).decode(FORMAT)) #When we receive the answer from server, Importante corregir el recv para mostrar en pantalla lo que ha sucedido

with window("Simple GUI", width= 520, height= 677):
    for i in range(3):
    
        print("GUI is running---")
        set_window_pos("Simple GUI",0,0)
        add_separator()
        add_spacing(count=12)
        add_text("This is a simple text for this simple gui", color = [232,163,33])
        add_separator()
        add_text("Next command", color = [232,163,33])


sendPID()
start_dearpygui()
