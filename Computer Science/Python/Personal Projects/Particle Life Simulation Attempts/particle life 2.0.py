import tkinter as tk
from random import randint
from math import sqrt

window_size = 1000
window = tk.Tk()

SPEED_CAP = 0.05

FORCE_MULTIPLIER = 1

canvas = tk.Canvas(width=window_size, height=window_size, bg="black")
canvas.pack()

particle_half_size = 4

particles = []

class particle:
    def __init__(self, colour, radius):
        self.x = randint(1, window_size)
        self.y = randint(1, window_size)
        self.vx = 0
        self.vy = 0
        self.type = colour
        self.attractionRadius = radius
    
def rule(particles1, particles2, g):
    for i in range(len(particles1)):
        fx = 0
        fy = 0
        for j in range(len(particles2)):
            a = particles1[i]
            b = particles2[j]
            
            dx = a.x - b.x        
            dy = a.y - b.y
            
            d = sqrt(dx**2 + dy**2)
            
            if a.attractionRadius + b.attractionRadius > d > 0:
                F = FORCE_MULTIPLIER * g/d**2
                fx += F * dx
                fy += F * dy
        
        '''a.vx - (a.vx/30)
        a.vy - (a.vy/30)'''
        
        if d < a.attractionRadius + b.attractionRadius:
            
            a.vx = (a.vx + fx)
            a.vy = (a.vy + fy)
            a.x += a.vx
            a.y += a.vy
            
            if a.vx > SPEED_CAP:
                a.vx = SPEED_CAP
            if a.vx < -SPEED_CAP:
                a.vx = -SPEED_CAP
            
            if a.vy > SPEED_CAP:
                a.vy = SPEED_CAP
            if a.vy < -SPEED_CAP:
                a.vy = -SPEED_CAP
        
        if a.x <= 0 or a.x >= window_size:
            a.vx *= -1
            if a.x < 0:
                a.x = 0
            else:
                a.x = window_size
        if a.y <= 0 or a.y >= window_size:
            a.vy *= -1
            if a.y < 0:
                a.y = 0
            else:
                a.y = window_size
        
    round(a.x, 8)
    round(a.y, 8)
    
def create(amount, colour, radius):
    tempParticles = []
    for _ in range(amount):
        tempParticle = particle(colour, radius)
        tempParticles.append(tempParticle)
        particles.append(tempParticle)    

    return tempParticles

yellow = create(50, "yellow", 300)
blue = create(50, "blue", 200)
green = create(50, "green", 450)
red = create(50, "red", 200)

def update():
    #rule(yellow, yellow, -3)
    rule(yellow, blue, -2)
    rule(blue, yellow, 2)
    rule(blue, blue, -0.5)
    rule(green, green, -2.5)
    rule(green, yellow, 1)
    rule(yellow, green, -1.5)
    rule(blue, green, -5)
    rule(red, blue, -4)
    rule(red, yellow, -4)
    canvas.delete("particle")
    for particle in particles:
        canvas.create_rectangle(particle.x - particle_half_size, particle.y - particle_half_size,
                                particle.x + particle_half_size, particle.y + particle_half_size,
                                fill=particle.type,
                                tag="particle")
    window.update()

while True:
    update()





