import tkinter as tk
import random

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

UNIVERSAL_FORCE_MULTIPLIER = 0.2
UNIVERSAL_FORCE_CAP = 0.1
UNIVERSAL_VELOCITY_CAP = 0.1

G = 1

PARTICLE_SIZE = 6


window = tk.Tk()

canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
canvas.pack()

particles = []

class particle:
    def __init__(self, colour):
        self.x = random.randint(1, WINDOW_WIDTH)
        self.y = random.randint(1, WINDOW_HEIGHT)
        self.colour = colour
    
        self.dx = 0
        self.dy = 0
        self.fx = 0
        self.fy = 0
        
        match colour:
            #force attraction rules in order: yellow, blue, green
            
            case "yellow":
                self.type = 0
                self.rules = [-10, 2, - 4]
            case "blue":
                self.type = 1
                self.rules = [5, -2, 4]
            
    def update(self):
        self.fx = 0
        self.fy = 0
        for particle in particles:
            try:
                #forces in the x axis
                x1 = self.x
                x2 = particle.x
                
                rx = x1 - x2
                
                forcex = (G/(rx)) * UNIVERSAL_FORCE_MULTIPLIER * self.rules[particle.type]
                
                if x1 > x2:
                    self.fx += forcex
                else:
                    self.fx -= forcex
                    
                #forces in the y axis
                y1 = self.y
                y2 = particle.y
                
                ry = y1 - y2
                
                forcey = (G/(ry)) * UNIVERSAL_FORCE_MULTIPLIER * self.rules[particle.type]
                
                if y1 > y2:
                    self.fy += forcey
                else:
                    self.fy -= forcey
            except:
                pass
        
        if self.fx > UNIVERSAL_FORCE_CAP:
            self.fx = UNIVERSAL_FORCE_CAP
        if self.fy > UNIVERSAL_FORCE_CAP:
            self.fy = UNIVERSAL_FORCE_CAP
        
        self.dx += self.fx
        self.dy += self.fy
        
        if self.dx > UNIVERSAL_VELOCITY_CAP:
            self.dx = UNIVERSAL_VELOCITY_CAP
        if self.dy > UNIVERSAL_VELOCITY_CAP:
            self.dy = UNIVERSAL_VELOCITY_CAP
        
        if self.x <= 0 and self.dx < 0:
            self.x = 1
            self.dx *= -1
        if self.x >= WINDOW_WIDTH and self.dx > 0:
            self.x = WINDOW_WIDTH - 1
            self.dx *= -1
        if self.y <= 0 and self.dy > 0:
            self.y = 1
            self.dx *= -1
        if self.y >= WINDOW_HEIGHT and self.dy < 0:
            self.y = WINDOW_HEIGHT - 1
            self.dy *= -1
        
        self.x += self.dx
        self.y += self.dy
        
        
    def draw(self):
        halfSize = PARTICLE_SIZE/2
        canvas.create_rectangle(self.x - halfSize, self.y - halfSize,
                                self.x + halfSize, self.y + halfSize,
                                fill=self.colour,
                                tag="particle")

def update():
    canvas.delete("particle")
    for particle in particles:
        particle.update()
        particle.draw()
    window.update()

def create(colour, amount):
    for _ in range(amount):
        particles.append(particle(colour))

create("yellow", 3)
#create("blue", 200)


def main():
    while True:
        update()
        

main()
