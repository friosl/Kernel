import socket
import os

from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(500,500)
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
    #print(client.recv(2048).decode(FORMAT)) #When we receive the answer from server, Importante corregir el recv para mostrar en pantalla lo que ha sucedido

def interface():
    with window("Simple GUI", width= 400, height= 350):
        set_window_pos("Simple GUI",0,0)
        show_documentation()
        add_spacing(count=12)
        add_button("Submit", callback = submit_callback)
        start_dearpygui()       #Esto bloquea la app!
        #Y nada más se sigue ejecutando. Cómo lograr entonces que sí se cambie dinámicamente?
        # A punta de botones que llamen métodos o que ome? D:
        while True:
        #for i in range(3):    
            add_separator()  
            add_text("Entró aquí? jajajaj", color= [232,163,33])
            print("Sí entra pero no lo pinta a menos que llamemos render?")
            action = client.recv(2048).decode(FORMAT)
            #set_window_pos("Simple GUI",0,0)
            add_separator()            
            add_text(action, color = [232,163,33])
            add_separator()
            #add_text("Next command", color = [232,163,33])
            #Aquí ahora debemos actualizar la interfaz, después de recibir el mensaje que viene del kernel.

def submit_callback(sender,data):
    print("Bloquea")
    action = client.recv(2048).decode(FORMAT)
sendPID()
interface()
#start_dearpygui()
