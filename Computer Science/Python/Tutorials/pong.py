import tkinter as tk
import time
import random

window_width = 800
window_height = 600

window = tk.Tk()
canvas = tk.Canvas(window, width=window_width, height=window_height, bg="black")
canvas.pack()

paddle_speed = 20
ball_speed = 300

lastTime = time.time() % 60

def getTime():
    global lastTime
    deltaTime = (time.time() % 60) - lastTime
    lastTime = time.time() % 60
    return deltaTime

class paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

    def moveUp(self, event):
        print("Up")
        self.y -= paddle_speed

    def moveDown(self, event):
        print("Down")
        self.y += paddle_speed

    def draw(self):
        canvas.create_rectangle(self.x - self.width/2, self.y - self.height/2,
                                self.x + self.width/2, self.y + self.height/2,
                                fill = "white")

class ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y

        self.radius = radius
        
        self.vx = random.choice([-1, 1])
        self.vy = random.choice([-1, 1])

    def move(self, deltaTime):
        self.x += ball_speed * self.vx * deltaTime
        self.y += ball_speed * self.vy * deltaTime

    def draw(self):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           fill="white")
    def update(self, deltaTime):
        self.move(deltaTime)
        self.draw()

    def checkPaddle(self):
        if self.y - self.radius <= paddle1.y + paddle1.height / 2 and self.y + self.radius >= paddle1.y - paddle1.height / 2:
            if self.x - self.radius <= paddle1.x + paddle1.width / 2:
                self.x = paddle1.x + paddle1.width / 2 + self.radius + 1
                self.vx *= -1
        if self.y - self.radius <= paddle2.y + paddle2.height / 2 and self.y + self.radius >= paddle2.y - paddle2.height / 2:
            if self.x + self.radius >= paddle2.x - paddle2.width / 2:
                self.x = paddle2.x - paddle2.width / 2 - self.radius - 1
                self.vx *= -1


    def checkCollisions(self):
        if self.x <= 0:
            self.x = 1
            self.vx *= -1
        if self.x >= window_width:
            self.x = window_width - 1
            self.vx *= -1
        if self.y <= 0:
            self.y = 1
            self.vy *= -1
        if self.y >= window_height - 1:
            self.y = window_height - 1
            self.vy *= -1

        self.checkPaddle()
        
paddle1 = paddle(50, window_height/2, 20, 100)
paddle2 = paddle(window_width - 50, window_height/2, 20, 100)
ball = ball(window_width / 2, window_height / 2, 10)

window.bind("<W>", paddle1.moveUp)
window.bind("<S>", paddle1.moveDown)
window.bind("<Up>", paddle2.moveUp)
window.bind("<Down>", paddle2.moveDown)

def main():
    while True:
        deltaTime = getTime()
        lastTime = time.time()
        canvas.delete("all")
        paddle1.draw()
        paddle2.draw()
        ball.update(deltaTime)
        ball.checkCollisions()
        window.update()
        
main()
