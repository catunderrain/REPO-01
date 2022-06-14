import turtle
import math
turtle.Screen().bgcolor('black')
turtle.hideturtle()
turtle.color('red')
turtle.pensize(3)
turtle.right(1)
turtle.speed(0)

n = 20
d = 10
r = (d/2)/math.sin(math.radians(180/n))
print(r)
turtle.begin_fill()


def circle():
    for i in range(n):
        turtle.forward(d)
        turtle.right(360/n)


circle()
# turtle.penup()
turtle.right(90)
turtle.forward(r)
turtle.left(90)
turtle.forward(2*r)
turtle.left(90)
turtle.forward(r)
turtle.right(90)
turtle.pendown()
circle()

# turtle.penup()
turtle.forward(d/2)
turtle.right(90)
turtle.forward(r + r*math.cos(math.radians(45)))
turtle.left(90)
turtle.forward(r*math.cos(math.radians(45)))
turtle.pendown()
turtle.right(135)
turtle.forward((r + r*math.cos(math.radians(45)))*math.sqrt(2))
turtle.right(90)
turtle.forward((r + r*math.cos(math.radians(45)))*math.sqrt(2))
turtle.end_fill()


turtle.exitonclick()
