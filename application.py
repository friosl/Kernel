import socket
import os
from datetime import datetime
from datetime import date
from os import path
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

pid = os.getpid() #Process ID

HEADER = 16
PORT   = 5051
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname()) #Nombre e IP de ntro pc
gui_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5050
ADDR= (HOST,PORT)
gui_send.connect(ADDR)