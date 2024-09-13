#particle life simulation attempt 4

import tkinter as tk
import random

window = tk.Tk()
canvas = tk.Canvas(window)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PARTICLE_SIZE = 8
FORCE_RADIUS = 500
FORCE_MULTIPLIER = 1/5
FRACTIONAL_SPEED_DECREASE = 1/10

window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
canvas.config(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
canvas.pack()

class particle:
    def __init__(self, x, y, vx, vy, colour, rules):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rules = rules
        self.colour = colour
    
    def update(self):
        canvas.create_oval(self.x - PARTICLE_SIZE/2, self.y - PARTICLE_SIZE/2,
                            self.x + PARTICLE_SIZE/2, self.y + PARTICLE_SIZE/2,
                            fill=self.colour)

    def getResultant(self):
        for particle in particles:
            if particle != self:
                d = ((particle.x - self.x)**2 + (particle.y - self.y)**2)**1/2
                
                if d <= FORCE_RADIUS and d != 0:
                    f = 1/(d**2) * self.rules[particle.colour]

                    fx = f * (particle.x - self.x) * FORCE_MULTIPLIER
                    fy = f * (particle.y - self.y) * FORCE_MULTIPLIER

                    self.vx += fx
                    self.vy += fy

                    self.vx -= FRACTIONAL_SPEED_DECREASE * self.vx
                    self.vy -= FRACTIONAL_SPEED_DECREASE * self.vy
                    
    def updatePosition(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0:
            self.x = 0
            self.vx *= -1
        if self.x >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
            self.vx *= -1
        if self.y <= 0:
            self.y = 0
            self.vy *= -1
        if self.y >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.vy *= -1


def ranVel():
    ran = random.random()
    ranSign = random.choice([-1, 1])

    return ran * ranSign

def ranf():
    ranf = 0
    while ranf == 0:
        ranf = random.random() * 10
    
    return ranf

particles = []

for i in range(100):
    particles.append((particle(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), ranVel(), ranVel(),
                                "yellow", {"yellow": 4, "red": ranf(), "blue": -2, "green": ranf()})))
for i in range(100):
    particles.append((particle(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), ranVel(), ranVel(),
                                "blue", {"yellow": 5, "red": ranf(), "blue": -0.1, "green": ranf()})))
'''for i in range(50):
    particles.append((particle(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), ranVel(), ranVel(),
                                "red", {"yellow": ranf(), "red": ranf(), "blue": ranf(), "green": ranf()})))
for i in range(50):
    particles.append((particle(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), ranVel(), ranVel(),
                                "green", {"yellow": ranf(), "red": ranf(), "blue": ranf(), "green": ranf()})))'''


def update():
    canvas.delete("all")
    for particle in particles:
        particle.getResultant()
        particle.updatePosition()
        particle.update()

    canvas.update()
    window.update()

def main():
    while True:
        update()

window.update()
main()
