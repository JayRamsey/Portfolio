import turtle
import numpy
import random

turtle.speed(0)
turtle.bgcolor("dark blue")
turtle.color("red")
turtle.fillcolor("red")

def draw_shape(size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.begin_fill()
    turtle.setheading(60)
    turtle.forward(2 * numpy.sqrt(2 * (size * size)))
    #turtle.setheading(90)
    turtle.circle(size, 230)
    turtle.setheading(90)
    turtle.circle(size, 230)
    turtle.forward(2 * numpy.sqrt(2 * (size * size)))
    turtle.end_fill()


for _ in range(20):
    draw_shape(random.randint(5, 30), random.randint(-300, 300), random.randint(-300, 300))