import turtle

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    my_points = [[-300, -200], [0, 300], [300, -200]]
    sierpinski(my_points, 4, t)
    
    wn.exitonclick()

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    x_middle = (p1[0]+p2[0])/2
    y_middle = (p1[1]+p2[1])/2
    mid = [x_middle, y_middle]
    return mid

def sierpinski(points, degree, my_turtle):
    color_list = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_list[degree], my_turtle)
    if degree > 0:
        sierpinski ([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1, my_turtle)
        sierpinski ([points[1], get_mid(points[1], points[2]), get_mid(points[1], points[0])], degree-1, my_turtle)
        sierpinski ([points[2], get_mid(points[2], points[1]), get_mid(points[2], points[0])], degree-1, my_turtle)

if __name__ == '__main__':
    main()