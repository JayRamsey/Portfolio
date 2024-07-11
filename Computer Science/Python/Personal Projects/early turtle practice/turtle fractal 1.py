import turtle

turtle.bgcolor("black")
turtle.left(90)
turtle.speed(0)
turtle.tracer()


def new_fib_sequence(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    n2 = 1

    for i in range(40):
        turtle.color(color)

        size = n2
        sides = 7
        angle = ((sides - 2) * 180) / sides

        for i in range(sides + 1):
            turtle.forward(size)
            turtle.right(180 - angle)

        n1 = n2/4
        n2 = n2 + n1

# instigating:


turtle.pensize(2)
#new_fib_sequence(2, 2, "red")
#new_fib_sequence(-2, -2, "cyan")
new_fib_sequence(0, 0, "white")

turtle.done()