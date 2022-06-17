from os import times
from tkinter import *
import datetime
from time import sleep
#
screen = Tk()
screen.geometry('1200x500')
screen.title('Time')
#


def getday():
    dt = datetime.datetime.now()
    timestatus = Label(text=dt).place(x=10, y=10)
    sleep(1)


getday()
screen.mainloop()
