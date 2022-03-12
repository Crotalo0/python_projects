import turtle
from random import randrange

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0.1)
    t.pensize(3)
    t.ht()

    x1 = -1000
    x2 = 1000
    y1 = 0
    y2 = 0
    x_array = []
    t.up()
    t.goto(x1, y1)
    t.down()

    array = mountain(x1, y1, x2, y2, 6, t, x_array)
    random_mountain(array , t)
    t.goto(x2, y2)

    wn.exitonclick()

def draw_line(x, y, turtle):
    turtle.goto(x, y)

def get_mid(p1, p2):
    x_middle = (p1[0]+p2[0])/2
    y_middle = (p1[1]+p2[1])/2
    return [x_middle, y_middle]

def mountain(x1, y1, x2, y2, degree, turtle, x_coord):
    draw_line(x2, y2, turtle)
    x_curr = turtle.xcor()
    x_coord.append(x_curr)
    
    if degree > 0:
        middle_point = get_mid([x1, y1], [x2, y2])
        x_mid = middle_point[0]
        y_mid = middle_point[1]
        
        mountain(x2, y2, x_mid, y_mid, degree-1, turtle, x_coord)
        mountain(x_mid, y_mid, x1, y1, degree-1, turtle, x_coord)
    
    return x_coord

def random_mountain(x_points, turtle):
    x_punti = []
    for i in x_points:
        if i not in x_punti:
            x_punti.append(i)

    x_punti.sort()

    turtle.up()
    turtle.goto(-1000, 0)
    turtle.down()
    for i in x_punti:
        y_random = randrange(50, 150)
        turtle.goto(i, y_random)   

    

if __name__ == "__main__":
    main()