import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import socket
import os 


pid = os.getpid() #Process ID

HEADER = 1024
PORT   = 5050
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname()) #Nombre e IP de ntro pc


logs_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR= (HOST,PORT)
logs_send.connect(ADDR)

print("Sending message")
msg="Log"
logs_send.send(msg.encode(FORMAT))

def backup_logs_read():
    logs_here.delete('1.0',END)
    back_up_file = open("logs_backup.txt", 'r')
    log_information = back_up_file.read()
    print(log_information)
    logs_here.insert(tk.END, log_information)
    log_information = ""
    back_up_file.close()


def backup_logs_write():
    back_up_file = open("logs_backup.txt", 'a')


win = Tk()

win.geometry("150x300")

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

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

win.mainloop()

