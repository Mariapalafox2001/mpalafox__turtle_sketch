from turtle import *
import math


screen = Screen()
screen.title("Turtle sketcher")
screen.bgcolor("#ffffe2")

artist = Turtle()
artist.color("Blue")
artist.pensize(2)
artist.speed(0)
artist.shape("turtle")
# shape can be arrow, circle, square, turtle

# Define some Functions!
def go_up():
	artist.setheading(90)
	artist.forward(10)

def go_down():
	artist.setheading(270)
	artist.forward(10)
	
def go_right():
	artist.setheading(0)
	artist.forward(10)

def go_left():
	artist.setheading(180)
	artist.forward(10)

def draw_star():
	artist.color("red")
	for x in range(5):
		artist.forward(50)
		artist.left(144)
	artist.color("Blue")

def draw_heart():
	artist.left(45)
	artist.forward(10*math.sqrt(2))
	artist.forward(10*math.sqrt(2))
	artist.forward(10*math.sqrt(2))
	artist.forward(10*math.sqrt(2))
	artist.left(45)
	artist.forward(10)
	artist.forward(10)
	artist.left(63)
	artist.forward(10*math.sqrt(1**2+(0.5)**2))
	artist.left(27)
	artist.forward(10)
	artist.left(27)
	artist.forward(10*math.sqrt(1**2+(0.5)**2))
	artist.left(63-45)
	artist.forward(10*math.sqrt(2))

	artist.right(90)
	artist.forward(10*math.sqrt(2))
	artist.left(63-45)
	artist.forward(10*math.sqrt(1**2+(0.5)**2))
	artist.left(27)
	artist.forward(10)
	artist.left(27)
	artist.forward(10*math.sqrt(1**2+(0.5)**2))
	artist.left(63)
	artist.forward(10)
	artist.forward(10)
	artist.left(45)
	artist.forward(10*math.sqrt(2))
	artist.forward(10*math.sqrt(2))
	artist.forward(10*math.sqrt(2))
	artist.forward(10*math.sqrt(2))
	artist.left(45)				

def clear_screen(x,y):
	screen.reset()
	artist.color("Blue")
	artist.pensize(2)
	artist.speed(0)


		

# Bind these functions to events
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")
screen.onkeypress(draw_star,"z")
screen.onkeypress(draw_heart,"h")

screen.onclick(clear_screen)

screen.listen()

mainloop()
