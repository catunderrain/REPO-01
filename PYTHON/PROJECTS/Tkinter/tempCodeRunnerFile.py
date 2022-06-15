from tkinter import *
import csv
#
screen = Tk()
screen.geometry('1200x500')
screen.title('Get Information')
#
direct = open('python/projects/tkinter/directory.csv', 'r')
#


def getdata():
    name = getname.get()
    info = ''
    for row in direct:
        if name in row:
            info = row
    data = Label(screen, text=str(info))
    data.place(x=30, y=80)
    direct.close()


# nhap ten
getname = Entry(text='')
getname.place(x=30, y=20, width=200, height=20)

# nut nhan
butdata = Button(text='Get', command=getdata)
butdata.place(x=30, y=50)
#
screen.mainloop()
