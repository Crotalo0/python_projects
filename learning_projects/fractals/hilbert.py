import turtle

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-400,400)
    t.pendown()
    t.speed(0.1)

    size = 10
    wn.screensize(size*63,size*63)

    hilbert_curve(size,2,90,t)

    wn.exitonclick()

def hilbert_curve(size,iter,angle,turtle):
    if iter == 0:
        return
    turtle.right(angle)
    hilbert_curve(size,iter - 1, -angle,turtle)
    turtle.forward(size)
    turtle.left(angle)
    hilbert_curve(size,iter - 1, angle,turtle)
    turtle.forward(size)
    hilbert_curve(size,iter - 1, angle,turtle)
    turtle.left(angle)
    turtle.forward(size)
    hilbert_curve(size,iter - 1, -angle,turtle)
    turtle.right(angle)

if __name__ == "__main__":
    main()