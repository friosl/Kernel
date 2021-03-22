import socket
import os
from os import path
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

def choose_process(event):
    selection = event.widget.get()
    if(selection == "Open app"):
        open_application()
    elif(selection == "Close app"):
        close_application()
    elif(selection == "Folder"):
        create_folder()
    else: 
        print("No valid option")
    

def open_application():
    pass

def close_application():
    pass


def create_folder():
    open_new_window = tk.Toplevel(window)
    open_new_window.title("New window")
    create_lable = tk.Label(open_new_window, text="Manage Folder", fg="black", font=("Arial", 15))
    folder_name = ttk.Entry(open_new_window)
    create_boton = tk.Button(open_new_window, text= "Create Folder", command = lambda: make_folder(folder_name.get()))
    delete_boton = tk.Button(open_new_window, text= "Delete Folder", command = lambda: delete_folder(folder_name.get()))

    open_new_window.geometry("150x300")

    create_lable.pack()
    folder_name.pack()
    create_boton.pack()
    delete_boton.pack()



def make_folder(folder_name):
    if folder_name != "":
        if path.exists(folder_name):
            pass
        else: 
            os.mkdir(folder_name)

def delete_folder(folder_name):
    if folder_name != "":
        if path.exists(folder_name):
            os.rmdir(folder_name)


def submit_callback(sender,data):
    print("Bloquea")
    action = client.recv(2048).decode(FORMAT)
sendPID()

window = Tk()
window.title("Sistemas Operativos")
window.state('zoomed')

list_title = tk.Label(window, text="Select one:", fg="black", )
list_title.config(anchor=CENTER)
list_title.pack()

lista = ttk.Combobox(window, values=["Open app", "Close app", "Folder"])
lista.pack()
lista.current()
lista.bind("<<ComboboxSelected>>", choose_process)

window.mainloop()





