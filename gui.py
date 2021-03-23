import socket
import os
from datetime import datetime
from datetime import date
from os import path
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randrange

pid = os.getpid() #Process ID

HEADER = 1024
PORT = 5050
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname()) #Nombre e IP de ntro pc
gui_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR= (HOST,PORT)
gui_send.connect(ADDR)
print("GUI binded to port 5051 and host is the same, listening")

msg="Gui"
gui_send.send(msg.encode(FORMAT))


def sendPID():
    message = str(pid).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length)) #Adding blankspaces
    gui_send.send(send_length)
    gui_send.send(message) 
    #print(client.recv(2048).decode(FORMAT)) #When we receive the answer from server, Importante corregir el recv para mostrar en pantalla lo que ha sucedido

def choose_process(event):
    selection = event.widget.get()
    if(selection == "Open app"):
        open_application()
    elif(selection == "Close app"):
        close_application()
    elif(selection == "Folder"):
        folder_popup()
    else: 
        print("No valid option")
    

def open_application():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"
    
    default_message = "status:"+strstatus+",cmd:send,src:GUI,dst:Application,msg:'\log: " + current_time + " "+ current_date+ ",OPEN APP"
    message = default_message.encode(FORMAT)
    #msg_length = len(message)
    #send_length = str(msg_length).encode(FORMAT)
    #send_length += b' '*(HEADER-len(send_length)) #Adding blankspaces
    #gui_send.send(send_length)
    gui_send.send(message)
    #Response (Message was received) 
    #print(client.recv(2048).decode(FORMAT))

def close_application():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"
    default_message = "status:"+strstatus+",cmd:send,src:GUI,dst:Application,msg:'\log: " + current_time + " "+ current_date + ",CLOSE APP"
    message = default_message.encode(FORMAT)
    gui_send.send(message)

def folder_popup():
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
            now = datetime.now()
            today = date.today()
            current_time = now.strftime("%H:%M:%S")
            current_date = today.strftime("%d/%m/%Y")
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC" #MESSAGE PROCESSED
                os.mkdir(folder_name)
            elif(status==8 or status==9):
                strstatus="BUSY" #MESSAGE BUSY
            elif(status==10):
                strstatus="ERROR" #MESSAGE ERROR

            default_message = "status:"+strstatus+",cmd:send,src:GUI,dst:log,msg:'\log: " + current_time + " "+ current_date + " CREATE FOLDER"
            message = default_message.encode(FORMAT)
            gui_send.send(message)

def delete_folder(folder_name):
    if folder_name != "":
        if path.exists(folder_name):
            now = datetime.now()
            today = date.today()
            current_time = now.strftime("%H:%M:%S")
            current_date = today.strftime("%d/%m/%Y")
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
                os.rmdir(folder_name)
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"
            default_message = "status:"+strstatus+",cmd:send,src:GUI,dst:log,msg:'\log: " + current_time + " "+ current_date + " DELETE FOLDER"
            message = default_message.encode(FORMAT)
            gui_send.send(message)
#sendPID()

def backup_logs_read():
    logs_here.delete('1.0',END)
    back_up_file = open("logs_backup.txt", 'r')
    log_information = back_up_file.read()
    print(log_information)
    logs_here.insert(tk.END, log_information)
    back_up_file.close()
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

wrapper1 = LabelFrame(window)
wrapper2 = LabelFrame(window)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT)

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")
wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)


logs_history_label = tk.Label(wrapper1, text="Logs History", fg="black", font=("Arial", 15))
logs_history_label.pack()

logs_here = tk.Text(wrapper1)
logs_here.pack()

update_button = tk.Button(wrapper2,text= "Update Logs", command = backup_logs_read)
update_button.pack()
window.mainloop()




