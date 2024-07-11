import turtle

import random

t = turtle.Turtle()
t.speed(0)
t.width(1)
t.color("red")

turtle.bgcolor("black")

def draw_shape():
    
    for i in range(120):

        t.forward(i)
        
        
        t.penup()
        
        t.goto(0, 0)
        t.right(8)
        
        t.pendown()


draw_shape()

turtle.done()