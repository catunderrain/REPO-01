import turtle
import random
scr = turtle.Screen()
scr.bgcolor('#000000')
turtle.hideturtle()
turtle.pensize(2)

for i in range(0, 20):
    turtle.color('#' + str(random.randint(100000, 999999)))
    turtle.forward(100)
    turtle.right(72)

turtle.exitonclick()
