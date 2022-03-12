import turtle
wn = turtle.Screen()
j = turtle.Turtle()
j.speed(30)
j.hideturtle()
j.pensize(3.1415)

k = turtle.Turtle()
k.speed(30)
k.color("red")
k.hideturtle()
k.pensize(3.1415)

for i in range (200):
    j.left(58)
    j.forward(i)
    
    k.left(58.1)
    k.forward(i)
wn.exitonclick()
