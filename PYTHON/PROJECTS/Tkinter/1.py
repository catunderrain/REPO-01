from tkinter import *
#


def Call():
    msg = Label(window, text='Pressed!')
    msg.place(x=30, y=50)
    button['bg'] = 'blue'
    button['fg'] = 'white'
    button['relief'] = 'flat'
    button['justify'] = 'cendter'


def Ex():
    exit()


#
window = Tk()
window.title('Sample')
window.geometry('1000x600')
#
button = Button(text='Click', command=Call)
button.place(x=30, y=20, width=120, height=25)
#
button2 = Button(text='Exit', command=Ex)
button2.place(x=30, y=80, width=120, height=25)
#
box = Entry(text='say')
box.place(x=30, y=120)
#
out = Message(text='End!')
out.place(x=30, y=150)
#
lis = Listbox()
lis.place(x=30, y=200)
#
window.mainloop()
