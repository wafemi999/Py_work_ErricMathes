from turtle import * 
play = Screen()

myPen = Turtle()

#Drawing the Rectangular shape

for i in [1, 2]:
	myPen.pencolor("red")
	myPen.forward(300)
	myPen.left(90)
	myPen.forward(150)
	myPen.left(90)
	
myPen.forward(300)
myPen.pencolor("white")
myPen.forward(90)


#drawing the triangle

for j in [0, 1, 2]:
	myPen.pencolor("red")
	myPen.forward(175)
	myPen.left(120)


myPen.color("white")
myPen.left(180)
myPen.forward(45)


#for the circular shape:
myPen.color("yellow")
myPen.shape("circle")
myPen.shapesize(8,15,1)
myPen.fillcolor("")
play.exitonclick()



