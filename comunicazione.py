from tkinter import *
from tkinter import Tk
from tkinter import ttk, StringVar
import serial.tools.list_ports

print(list(serial.tools.list_ports.comports()))
print([comport.device for comport in serial.tools.list_ports.comports()])

for comport in serial.tools.list_ports.comports():
    print(comport.device)
