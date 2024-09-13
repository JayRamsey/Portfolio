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
FOCAL_LENGTH = 1000
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

def generateWarpEffect():
    lineCount = 800
    polyCount = 300
    maxLineDepth = 12000
    minLineDepth = 50
    maxLineLength = 1000
    minLineLength = 400
    maxPolyDepth = 10000
    minPolyDepth = 8000
    maxPolyLength = 8000
    minPolyLength = 6000
    
    polyColour = 204, 255, 255
    
    areaMultipler = 3
    
    maxPolyXOffset = 10
    maxPolyYOffset = 10
    
    
    global OBJECTS
    
    for i in range(lineCount):
        x = random.randint(-SCREEN_WIDTH * areaMultipler, SCREEN_WIDTH * areaMultipler)
        y = random.randint(-SCREEN_HEIGHT * areaMultipler, SCREEN_HEIGHT * areaMultipler)
        z1 = random.randint(minLineDepth, maxLineDepth)
        z2 = z1 - random.randint(minLineLength, maxLineLength)
        
        OBJECTS.append(Line([x, y, z1], [x, y, z2]))
    
    for i in range(polyCount):
        x1 = random.randint(-SCREEN_WIDTH * areaMultipler, SCREEN_WIDTH * areaMultipler)
        y1 = random.randint(-SCREEN_HEIGHT * areaMultipler, SCREEN_HEIGHT * areaMultipler)
        x2 = x1 + random.randint(-maxPolyXOffset, maxPolyXOffset)
        y2 = y1 + random.randint(-maxPolyYOffset, maxPolyYOffset)        
        z1 = random.randint(minPolyDepth, maxPolyDepth)
        z2 = z1 - random.randint(minPolyLength, maxPolyLength)
        
        OBJECTS.append(Poly([[x1, y1, z1],[x2, y2, z1],[x2, y2, z2],[x1, y1, z2]], polyColour))
    
    

def main():
    generateWarpEffect()
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