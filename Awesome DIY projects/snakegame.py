#Snake Game

import turtle
import random
import time

#setting up the screen
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor("Green")
wn.title("Snake Game")

#Draw border
borderpen = turtle.Turtle()
borderpen.color("white")
borderpen.speed(0)
borderpen.penup()
borderpen.setpos(-300, 300)
borderpen.pendown()
for i in range(4):
    borderpen.fd(600)
    borderpen.rt(90)
borderpen.ht()

#Snake class
class Snake(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.penup()
        self.setpos(0, 0)
        
#instantiating head of snake
head = Snake()
head.color("grey")
head.setheading(2)

#snake segments
snake_segments=[]

#Making food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.speed(0)
food.penup()
food.setpos(random.randint(-260, 260), random.randint(-260, 260))
        
#Creating movement functions
def down():
    head.seth(270)
def up():
    head.seth(90)
def left():
    head.seth(180)
def right():
    head.seth(0)

#function to check for collisions between snake and food
def eat():
    if head.distance(food) < 20:
        food.setpos(random.randint(-260, 260), random.randint(-260, 260))
        snake_segments.append(Snake())
    if len(snake_segments)>0:
        snake_segments[0].setpos(head.xcor(), head.ycor())

    if len(snake_segments)>1:
        for segment in range(len(snake_segments)-1,0,-1):
            snake_segments[segment].setpos(snake_segments[segment-1].xcor(), snake_segments[segment-1].ycor())
    
#function to check if snake passes boundry
def collision():
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        head.home()
        head.setheading(2)
        for i in range(len(snake_segments)):
            snake_segments[0].ht()
            snake_segments.remove(snake_segments[0])
        print(len(snake_segments))
        
        
#Creating screen events
turtle.listen()
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")


wn.tracer(0)

#Game mainloop
while True:

    
    eat()
    time.sleep(0.1)
    if head.heading() == 0.0:
        head.setpos(head.xcor()+20, head.ycor())
    elif head.heading() == 90.0:
        head.setpos(head.xcor(), head.ycor()+20)
    elif head.heading() == 180.0:
        head.setpos(head.xcor()-20, head.ycor())
    elif head.heading() == 270.0:
        head.setpos(head.xcor(), head.ycor()-20)
    collision()
    
    wn.update()

wn.mainloop()
