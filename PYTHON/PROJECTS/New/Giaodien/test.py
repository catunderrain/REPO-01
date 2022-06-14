from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
#----------------------------------------------------------
window = Tk()
window.geometry('500x500')
window.title('TEST TKINTER')
#----------------------------------------------------------
def but1():
    exit()
#----------------------------------------------------------
lb1 = tkinter.Label(window, text = 'Title 1', bg = 'blue', fg = 'white', font = ('Arial', 10))
lb1.grid(column = 1, row = 1)

lb11 = Combobox(window, width = 12)
lb11.grid(column = 1, row = 2)
lb11['value'] = ('one', 'two', 'three')
lb11.current(0)
#----------------------------------------------------------
lb2 = tkinter.Label(window, text = 'Title 2', bg = 'red', fg = 'white', font = ('Arial', 10))
lb2.grid(column = 2, row = 1)

lb22 = Combobox(window, width = 12)
lb22.grid(column = 2, row = 2)
lb22['value'] = ('one', 'two', 'three')
lb22.current(1)
#----------------------------------------------------------
lbx = tkinter.Label(window, text = 'Hello!', bg = 'black', fg = 'white', font = ('Arial', 25))
lbx.place(x = 210, y = 210)
#----------------------------------------------------------
but = Button(window, text = 'Click here', command = but1)
but. place(x = 210, y = 300)
#----------------------------------------------------------
window.mainloop()
