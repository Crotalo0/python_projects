import turtle
def main():
    wn=turtle.Screen()
    wn.setworldcoordinates(-400,-400,400,400)
    p=turtle.Turtle()

    with open('mystery.txt','r') as f:
        coord = f.readline()
        while coord:
            val=coord.split()
            if val[0]=='UP':
                p.up()
            elif val[0]=='DOWN':
                p.down()
            else:
                p.goto(int(val[0]),int(val[1]))
            coord = f.readline()
    wn.exitonclick()
    
            
if __name__=='__main__':
    main()