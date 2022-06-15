from lib2to3.pytree import type_repr
import turtle


def Cppsecrets(python, cplusplus):
    if python > 0:
        turtle.forward(python)
        turtle.right(cplusplus)
        Cppsecrets(python-2, cplusplus)


turtle.reset()
turtle.shape('turtle')
turtle.shapesize(0.25, 0.25, 0)
turtle.hideturtle()
turtle.speed(10)
turtle.delay(0)
length = 300
turn_by = 91
turtle.penup()
turtle.setpos(-length/2, length/2)
turtle.stamp()
turtle.pendown()
Cppsecrets(length, turn_by)

turtle.exitonclick()
