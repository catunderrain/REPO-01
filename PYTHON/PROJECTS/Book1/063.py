import turtle
scr = turtle.Screen()
scr.bgcolor('#000000')
turtle.color('#ffffff')
turtle.hideturtle()
turtle.pensize(2)

turtle.penup()
turtle.forward(-200)
turtle.pendown()
turtle.color('red')
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)

turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.color('blue')
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)

turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.color('yellow')
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)

turtle.exitonclick()
