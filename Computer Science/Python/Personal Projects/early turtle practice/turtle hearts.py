import turtle
import random

turtle.bgcolor("black")
turtle.color("red")
turtle.pensize(2)
turtle.tracer()
turtle.speed(1000)

def draw_shape(size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.setheading(45)
    turtle.forward(size)
    for i in range(76):
        turtle.forward(size/48)
        turtle.left(3)
    turtle.setheading(turtle.tiltangle()+90)
    for i in range(76):
        turtle.forward(size/48)
        turtle.left(3)
    turtle.goto(x, y)
    turtle.end_fill()


for i in range(25):
    draw_shape(random.randint(10, 40), random.randint(-300, 300), random.randint(-300, 300))

turtle.done()
