import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')

t.color('orange')
t.pensize(5)
t.penup()
t.setpos(-500, 0)
t.pendown()
t.speed(0)          #fastest draw setting, 10 is slowest

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        new_func(t, order, size)

def new_func(t, order, size):
    for angle in [60, -120, 60, 0]:
        koch(t, order - 1, size // 3)
        t.left(angle)

size = 1000
order = 3
koch(t, order, size)

wn.exitonclick()