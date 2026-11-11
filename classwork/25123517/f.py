from turtle import *
tracer(0)
screensize(5000,5000)
scale = 10

pensize(3)
color('red')
for _ in range(6):
    fd(33*scale)
    rt(90)
    fd(20*scale)
    rt(90)
up()
fd(3*scale)
rt(90)
fd(9*scale)
lt(90)
down()
for _ in range(6):
    fd(24*scale)
    rt(90)
    fd(25*scale)
    rt(90)

pensize(0)
color('grey')
for x in range(-100,100):
    up()
    goto(x*scale, -100*scale)
    down()
    goto(x*scale, 100*scale)
for y in range(-100,100):
    up()
    goto(-100*scale, y*scale)
    down()
    goto(100*scale,y*scale)

input()