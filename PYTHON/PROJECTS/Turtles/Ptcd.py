import turtle
import time
#
ts = 0
te = 10
t = te - ts
tdiv = 1
s = 200
v = s/t  # 144m/s
del_s = v*tdiv  # 2m
snum = int(s/del_s)
tnum = int((te - ts)/tdiv)
print(tnum)
t_arr = [round(tdiv*k, 2) for k in range(0, tnum + 1)]
print(t_arr)
scr = turtle.Screen()
scr.bgcolor('white')
turtle.shape('circle')
turtle.shapesize(0.5, 0.5, 0)

# 100m
turtle.delay()
for i in range(snum):
    turtle.delay(0)
    turtle.fd(del_s)
    time.sleep(tdiv)


turtle.exitonclick()
