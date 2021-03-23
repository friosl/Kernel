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

print("Logs binded in port 5050")
msg="Log"
logs_send.send(msg.encode(FORMAT))

def backup_logs_read():
    #logs_here.delete('1.0',END)
    back_up_file = open("logs_backup.txt", 'r')
    log_information = back_up_file.read()
    print(log_information)
    #logs_here.insert(tk.END, log_information)
    log_information = ""
    back_up_file.close()


def backup_logs_write(log):
    back_up_file = open("logs_backup.txt", 'a')
    back_up_file.write(log+"\n")
    back_up_file.close()

while True:
    msg = logs_send.recv(HEADER).decode(FORMAT)  
    print(msg)
    backup_logs_write(msg)
