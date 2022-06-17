from os import times
from tkinter import *
import datetime
from time import sleep, time

from matplotlib.animation import TimedAnimation
#
screen = Tk()
screen.geometry('1200x500')
screen.title('Time')
#
dt = datetime.datetime.now()
timestatus = Label(text='asd').place(x=10, y=10)
screen.mainloop()
sleep(1)
timestatus = Label(text='asddsd').place(x=10, y=10)
screen.mainloop()
