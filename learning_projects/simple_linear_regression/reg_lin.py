#linear regression with turtle library
import turtle

def max(lst):
    x = lst[0]
    for i in lst:
        if i > x:
            x = i
    return x

def min(lst):
    x = lst[0]
    for i in lst:
        if i < x:
            x = i
    return x

def mean(lst):
    somma = 0
    for value in lst:
        somma = somma + value
    mean = somma/len(lst)
    return mean  

def retta(m,x,q):
    ya = m*x + q
    return ya

def datafile_read(file_name):
    """Input a .txt file with x and y in 2 columns."""
    print('Starting file read...')
    x=[]
    y=[]
    try:
        infile = open("labdata.txt", "r")
        line = infile.readline()
        while line:
            values = line.split()
            print(f"x: {values[0]}; y: {values[1]}")
            x.append(int(values[0]))
            y.append(int(values[1])) 
            line=infile.readline()
    except:
        print('Something went wrong while opening txt file.')
    finally:
        infile.close()
        print('Array x and y created.') 
        print('Opening procedure terminated.')
    return x,y

def plotRegression(data):
    """Plot done with turtle graphics."""
    x,y=datafile_read(data)
    x_mean = mean(x)
    y_mean = mean(y)
    
    xy_sum = 0
    for i in range(len(x)):
        prod = x[i] * y[i]
        xy_sum += prod
    
    xsq_sum = 0
    for i in range(len(x)):
        prod = x[i] * x[i]
        xsq_sum += prod
    
    m = (((xy_sum) - (x_mean*y_mean*len(x)))/((xsq_sum)-(len(x)*x_mean*x_mean)))
    #y1 = y_mean + m(x-x_mean)

    wn=turtle.Screen()
    wn.setworldcoordinates(min(x)-5,min(y)-5,max(x)+5,max(y)+5)
    p = turtle.Turtle()
    fit = turtle.Turtle()
    p.hideturtle()
    p.speed(100)
    fit.color('red')
    fit.hideturtle()
    fit.width(4)
    fit.speed(100)
    fit.up()
   
    for i in range(len(x)):
        p.up()
        p.goto(x[i],y[i])
        p.dot(10)
    
    for n in range(min(x)-10,max(x)+10):
        new_pos= (n,retta(m,n-x_mean,y_mean))
        fit.goto(new_pos)
        fit.down()

        
    wn.exitonclick()

def main():
     plotRegression('labdata.txt')

    
if __name__ == '__main__':
    main()
