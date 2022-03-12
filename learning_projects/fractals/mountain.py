import turtle
from random import randrange

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    my_points = [[-400,0],[400,0]]
    mountain(my_points, 3, t )

    wn.exitonclick()

def draw_line(points,turtle):
    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.goto(points[1][0],points[1][1])

def get_mid(p1,p2):
    x_middle = (p1[0]+p2[0])/2
    y_middle = (p1[1]+p2[1])/2
    mid = [x_middle,y_middle]
    return mid

def mountain(points, degree, turtle):
    turtle.stamp()
    draw_line(points, turtle)
    if degree > 0:
        mountain([points[0],get_mid(points[0],points[1])],degree-1,turtle)
        mountain([points[1],get_mid(points[1],points[0])],degree-1,turtle)


if __name__=="__main__":
    main()