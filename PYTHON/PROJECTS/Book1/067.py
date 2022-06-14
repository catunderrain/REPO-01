import turtle
#
scr = turtle.Screen()
scr.setup(width=1.0, height=1.0, startx=None, starty=None)
scr.bgcolor('#000000')
#
turtle.speed(0.0001)
turtle.pensize(4)
turtle.hideturtle()
#
n = 10
#


def randhex():
    import random
    def r(): return random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r(), r(), r())


#
while True:
    for i in range(0, 10):
        color = randhex()
        for i in range(0, n):
            turtle.color(color)
            turtle.forward(50)
            turtle.right(360/n)
        turtle.right(36)
