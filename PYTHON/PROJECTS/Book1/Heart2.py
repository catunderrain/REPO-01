import turtle
#
turtle.bgcolor("black")
#
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.pensize(6)
t.color("red")
#
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
#
t.penup()
t.goto(-90, -200)
t.pendown()
t.color('white')
t.write('30/4/1975', 'center', font=('Aria', 30))
#
turtle.exitonclick()
