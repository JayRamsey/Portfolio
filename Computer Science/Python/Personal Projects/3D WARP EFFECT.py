# import numpy
import random
import pygame
import pygame.locals

#global vars/ setup
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)

SCREEN_CENTRE_X = SCREEN_WIDTH / 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT /2
FOCAL_LENGTH = 500
OBJECTS = []
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Point:
    def __init__(self, pos: list[float, float, float]):
        self.x, self.y, self.z = pos
    
    def vector(self):
        return [self.x, self.y, self.z]

class Line:
    def __init__(self, pos1: list[float, float, float], pos2: list[float, float, float], colour = WHITE):
        self.point1 = Point(pos1)
        self.point2 = Point(pos2)
        self.colour = colour
    
    def draw(self):
        pygame.draw.line(SURFACE, self.colour, project3Dto2D(self.point1.vector()), project3Dto2D(self.point2.vector()))

class Poly:
    def __init__(self, points: list[Point], colour = (255, 255, 255)):
        self.points = points
        self.colour = colour

    def draw(self):
        points = list(map(project3Dto2D, self.points))
        pygame.draw.polygon(SURFACE, self.colour, points)


def project3Dto2D(pos):
    x, y, z = pos
    if z + FOCAL_LENGTH != 0:
        focalFactor = FOCAL_LENGTH/ (FOCAL_LENGTH + z)
    else:
        focalFactor = FOCAL_LENGTH/ (FOCAL_LENGTH + z + 1)
    newX = SCREEN_CENTRE_X + x * focalFactor
    newY = SCREEN_CENTRE_Y - y * focalFactor
    return [newX, newY]
   

def room(size):
    halfSize = size / 2
    doorFractionWidth = 1/3
    doorFractionHeight = 2/ 3
    
    #front face
    OBJECTS.append(Line([-halfSize, halfSize, 0], [halfSize, halfSize, 0]))
    OBJECTS.append(Line([halfSize, halfSize, 0], [halfSize, -halfSize, 0]))
    OBJECTS.append(Line([halfSize, -halfSize, 0], [-halfSize, -halfSize, 0]))
    OBJECTS.append(Line([-halfSize, -halfSize, 0], [-halfSize, halfSize, 0]))

    #back face
    OBJECTS.append(Line([-halfSize, halfSize, size], [halfSize, halfSize, size]))
    OBJECTS.append(Line([halfSize, halfSize, size], [halfSize, -halfSize, size]))
    OBJECTS.append(Line([halfSize, -halfSize, size], [-halfSize, -halfSize, size]))
    OBJECTS.append(Line([-halfSize, -halfSize, size], [-halfSize, halfSize, size]))
    
    #connecting lines
    OBJECTS.append(Line([-halfSize, halfSize, 0], [-halfSize, halfSize, size]))
    OBJECTS.append(Line([halfSize, halfSize, 0], [halfSize, halfSize, size])),
    OBJECTS.append(Line([halfSize, -halfSize, 0], [halfSize, -halfSize, size]))
    OBJECTS.append(Line([-halfSize, -halfSize, 0], [-halfSize, -halfSize, size]))
    
    #doorOutline
    doorHeight = doorFractionHeight * size
    doorWidth = doorFractionWidth * size
    OBJECTS.append(Poly([[-halfSize, -halfSize, 0.5 * (size - doorWidth)],
                         [-halfSize, -halfSize, 0.5 * (size - doorWidth) + doorFractionWidth],
                         [-halfSize, -halfSize + size * doorFractionHeight, 0.5 * (size - (size * doorFractionWidth)) + doorFractionWidth],
                         [-halfSize, -halfSize + size * doorFractionHeight, 0.5 * (size - (size * doorFractionWidth))]]))
    

    

def main():
    room(500)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        SURFACE.fill((0, 0, 0))
        
        for object in OBJECTS:
            object.draw()
        
        clock.tick(60)
        pygame.display.flip()


main()