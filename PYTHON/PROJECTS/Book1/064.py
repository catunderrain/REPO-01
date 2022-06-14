import turtle
scr = turtle.Screen()
scr.bgcolor('#000000')
turtle.color('#ffffff', 'red')
turtle.hideturtle()
turtle.pensize(2)
turtle.begin_fill()
for i in range(0, 5):
    turtle.forward(100)
    turtle.right(144)
turtle.color('white', 'red')
turtle.end_fill()

turtle.exitonclick()
