import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("black")

finish_line = turtle.Turtle()
finish_line.color("white")
finish_line.pensize(2)
finish_line.hideturtle()
finish_line.penup()
finish_line.forward(380)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(50)
finish_line.forward(-140)

start_line = turtle.Turtle()
start_line.color("red")
start_line.pensize(2)
start_line.hideturtle()
start_line.penup()
start_line.forward(-590)
start_line.pendown()
start_line.left(90)
start_line.forward(50)
start_line.forward(-140)


vittoria = turtle.Turtle()
vittoria.color("white")
vittoria.pensize(2)
vittoria.hideturtle()
vittoria.penup()
vittoria.left(90)
vittoria.forward(50)
vittoria.pendown()
vittoria.right(90)

mimmo = turtle.Turtle()
mimmo.shape("turtle")
mimmo.color("orange")
mimmo.penup()

mauro = turtle.Turtle()
mauro.shape("turtle")
mauro.color("cyan")
mauro.penup()

paulo = turtle.Turtle()
paulo.shape("turtle")
paulo.color("HotPink")
paulo.penup()

mauro.goto(-600,20)
mimmo.goto(-600,-20)
paulo.goto(-600,-60)

x1=[]
y1=[]
z1=[]

time.sleep(1)
vittoria.write("Ready...",move=False,align="left",font=("Arial",14,"normal"))
time.sleep(1)
vittoria.clear()
vittoria.write("...Set...",move=False,align="left",font=("Arial",14,"normal"))
time.sleep(1)
vittoria.clear()
vittoria.write("...GOOOO! :D",move=False,align="left",font=("Arial",14,"normal"))

for i in range(0,1500,1):
	x=random.randrange(1,5)
	y=random.randrange(1,5)
	z=random.randrange(1,5)
		
	mauro.forward(x)
	mimmo.forward(y)
	paulo.forward(z)
	print(x,y,z)
	x1.append(x)
	y1.append(y)
	z1.append(z)
	print(sum(x1),sum(y1),sum(z1))
	
	if sum(x1)<980 and sum(y1)>980 and sum(z1)<980:
		print("La tartaruga arancione ha vinto!")
		vittoria.clear()
		vittoria.write("La tartaruga arancione ha vinto! :D",move=False,align="left",font=("Arial",14,"normal"))
		mimmo.left(720)
		break
	elif sum(x1)>980 and sum(y1)<980 and sum(z1)<980:
		print("La tartaruga celeste ha vinto!")
		vittoria.clear()
		vittoria.write("La tartaruga celeste ha vinto! D:",move=False,align="left",font=("Arial",14,"normal"))
		mauro.right(720)
		break
	elif sum(x1)<980 and sum(y1)<980 and sum(z1)>980:
		print("La tartaruga rosa ha vinto!")
		vittoria.clear()
		vittoria.write("La tartaruga rosa ha vinto! D:",move=False,align="left",font=("Arial",14,"normal"))
		paulo.right(720)
		break
	elif sum(x1)==980 and sum(y1)== 980 and sum(z1)==980:
		print("Sono arrivate tutte assieme! Assurdo!")
		vittoria.clear()
		vittoria.write("Sono arrivate tutte assieme! Assurdo!",move=False,align="left",font=("Arial",14,"normal"))
		break
	elif sum(x1)==980 and sum(y1)== 980 and sum(z1)<980:
		print("Pareggio tra la celeste e la arancione! Incredibile!")
		vittoria.clear()
		vittoria.write("Pareggio tra la celeste e la arancione! Incredibile!",move=False,align="left",font=("Arial",14,"normal"))
		break
	elif sum(x1)==980 and sum(y1)< 980 and sum(z1)==980:
		print("Pareggio tra la celeste e la rosa! Incredibile!")
		vittoria.clear()
		vittoria.write("Pareggio tra la celeste e la rosa! Incredibile!",move=False,align="left",font=("Arial",14,"normal"))
		break
	elif sum(x1)<980 and sum(y1)== 980 and sum(z1)==980:
		print("Pareggio tra la arancione e la rosa! Incredibile!")
		vittoria.clear()
		vittoria.write("Pareggio tra la arancione e la rosa! Incredibile!",move=False,align="left",font=("Arial",14,"normal"))
		break
		
		
wn.exitonclick()


















