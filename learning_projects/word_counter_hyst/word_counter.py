import turtle

def word_counter(word):
    """Word counter with dictionaries."""
    counter = {}
    for char in word:
        if char.lower() in counter:
            counter[char.lower()]+=1
        else:
            counter[char.lower()]=1
    return counter

def hystogram(word):
    wn = turtle.Screen()
    p = turtle.Turtle()
    p.goto(0,0)
    p.speed(0)
    

    x = word_counter(word)
    keylist = list(x.keys())
    keylist.sort()
    value_list=x.values()

    wn.setworldcoordinates(0,0,len(value_list)*10+10,max(value_list)+max(value_list)/10)

    for i in keylist:
        p.left(90)
        p.forward(x[i])
        p.up()
        p.forward(x[i]/100)
        p.right(90)
        p.forward(3)
        p.write(f"{i},{x[i]}")
        p.right(180)
        p.forward(3)
        p.left(90)
        p.forward(x[i]/100)
        p.left(90)
        p.down()
        p.forward(10)
        p.right(90)
        p.forward(x[i])
        p.left(90) 

    wn.exitonclick()



def main():
    x = input('Input word: ')
    print(word_counter(x))
    hystogram(x)


if __name__=='__main__':
    main()