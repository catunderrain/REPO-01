import turtle
import math


turtle.Screen().bgcolor('black')
turtle.pensize(10)
turtle.Screen().setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.hideturtle()
turtle.speed(0)
d = 40
n = 12
w = 60
w2 = 360/n


def leaf():
    turtle.begin_fill()
    turtle.forward(d)
    turtle.left(w)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d*math.sqrt(2)/2)
    turtle.left(90)
    turtle.forward(d*math.sqrt(2)/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w/4)
    turtle.forward(d/2)
    turtle.left(w)
    turtle.forward(d)
    turtle.end_fill()


turtle.color('black', 'brown')
turtle.begin_fill()
for i in range(0, n):
    turtle.forward(d)
    turtle.right(w2)
turtle.end_fill()
turtle.color('black', 'yellow')

for i in range(0, n):
    leaf()
    turtle.right(w2)

turtle.exitonclick()
