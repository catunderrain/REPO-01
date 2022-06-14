import turtle
import random
scr = turtle.Screen()
scr.bgcolor('#000000')
turtle.color('#ffffff')
turtle.hideturtle()
turtle.pensize(2)

n = random.randint(3, 30)
fw = random.randint(10, 30)
angle = 360/n
for i in range(0, n):
    turtle.forward(fw)
    turtle.right(angle)


turtle.exitonclick()
