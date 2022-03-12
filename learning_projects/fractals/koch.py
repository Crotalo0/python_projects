import turtle

def main():
    wn = turtle.Screen()
    wn.bgcolor('black')

    tin = turtle.Turtle()
    tin.hideturtle()
    tin.color('yellow')
    tin.fillcolor('cyan')
    tin.pensize(1)
    tin.speed(0)
    
    size = 300
    tin.penup()
    tin.goto(-size/2, size/3)
    tin.pendown()

    tin.begin_fill()
    koch_snowflake(size,4,tin)
    tin.end_fill()

    wn.exitonclick()

def koch_curve(lenght,iter,t):
    if iter==0:
        t.forward(lenght)
    else: 
        for angle in [60, -120, 60, 0]:
            koch_curve(lenght//3, iter-1,t)
            t.left(angle)

def koch_snowflake(lenght, iter, t):
    koch_curve(lenght, iter, t)
    t.right(120)
    koch_curve(lenght, iter, t)
    t.right(120)
    koch_curve(lenght, iter, t)

if __name__ == "__main__":
    main()