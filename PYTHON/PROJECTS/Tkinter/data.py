from tkinter import *
import csv
#
screen = Tk()
screen.geometry('1200x500')
screen.title('Get Information')
#

#


def getdata():
    direct = open('python/projects/tkinter/directory.csv', 'r')
    info = ''
    name = getname.get()
    if name == '':
        data = Label(screen, text='')
        data.place(x=30, y=80, width=500, height=500)
    else:
        for row in direct:
            if name.lower() in row.lower():
                data = Label(screen, text=row)
                data.place(x=30, y=80, width=500, height=500)

    direct.close()


# nhap ten
getname = Entry(text='')
getname.place(x=30, y=20, width=200, height=20)

# nut nhan
butdata = Button(text='Get', command=getdata)
butdata.place(x=30, y=50)
#


screen.mainloop()
