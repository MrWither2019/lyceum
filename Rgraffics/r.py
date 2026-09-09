import turtle
t = turtle.Turtle()
t.speed(0)
t.color('blue')

def draw_square(a):
    t.right(90)
    t.forward(a / 2)
    t.left(90)
    for i in range(4):
        t.forward(a)
        t.left(90)

def drawt(n, length, pen):
    t.pensize(pen)
    if n == 0:
        return
    draw_square(length)
    t.forward(10)
    t.left(90)
    t.forward(length // 2)
    t.right(85)
    drawt(n - 1, length - 20, pen - 0.1)

t.penup()
t.lt(90)
t.pendown()

drawt(10, 200, 4)

turtle.done()