#Particle life simulation attempt

import random
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window)


particles = []
affectRadius = 100
forceMulti = 1000
particleSize = 8

screenWidth = 800
screenHeight = 800

window.geometry(f"{screenWidth}x{screenHeight}")
canvas.config(bg="black", width=screenWidth, height=screenHeight)
canvas.pack()

counts = [["red", 10], ["yellow", 30], ["blue", 40], ["green", 30]]

'''     red  yellow  green  blue
red     [                      ]
yellow  [                      ]
green   [                      ]
blue    [                      ]
'''

rules = [[1, -2, 3, 4],
         [-2, 5, -1, 6],
         [3. -1, -2, 1],
         [4, 6, 1, 0]]

def getPairPosValues(particle1, particle2):

    largerX = max(particle1.x, particle2.x)
    smallerX = min(particle1.x, particle2.x)
    largerY = max(particle1.y, particle2.y)
    smallerY = min(particle1.y, particle2.y)

    return largerX, largerY, smallerX, smallerY

def getDistance(particle1, particle2):

    largerX, largerY, smallerX, smallerY = getPairPosValues(particle1, particle2)

    return ((largerX - smallerX)**2 + (largerY - smallerY)) ** 1/2


class particle:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.vx = 0
        self.vy = 0

    def forceApply(self, particle):
        
        d = getDistance(self, particle)
        f = 1/d *  forceMulti

        dx = particle.x - self.x
        dy = particle.y - self.y

        fx = f * dx
        fy = f * dy

        self.vx += fx
        self.vy += fy

    def draw(self):
        canvas.create_oval(self.x - particleSize/2, self.y - particleSize/2,
                           self.x + particleSize/2, self.y + particleSize/2, fill=self.colour)

    def updatePos(self):
        self.x += self.vx
        self.y += self.vy

        self.draw()

    def update(self):
        for particle in particles:
            if particle != self and getDistance(self, particle) <= affectRadius:
                self.forceApply(particle)
                self.updatePos()


for n in counts:
    for i in range(n[1]):
        particles.append(particle(random.random() * screenWidth, random.random() * screenHeight, n[0]))

print(particles)

while True:
    canvas.delete("all")
    for particle in particles:
        particle.update()
        particle.draw()
    canvas.update()
    window.update()

