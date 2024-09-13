import pygame
import random
import numpy

screenwidth = 800
screenHeight = 800
minStreakLength = 75
maxStreakLength = 300
streakCount = 1000
closestStartZ = -200
furthestStartZ = 500
minCentreGap = 100
lineWidth = 2
colours = [(102, 153, 153), (204, 255, 255), (200, 200, 200), (51, 153, 255)]

pygame.init()
surface = pygame.display.set_mode((screenwidth, screenHeight))


lines = []
lineColours = []

for _ in range(streakCount):
    x = random.randint(-screenwidth/2, screenwidth/2)
    y = random.randint(-screenHeight/2, screenHeight/2)
    z = random.randint(closestStartZ, furthestStartZ)
    
    point1 = x, y, z
    point2 = x, y, z + random.randint(minStreakLength, maxStreakLength)
    
    lines.append([point1, point2])
    lineColours.append(random.choice(colours))
    
focalLength = 300


def project(point):
    x, y, z = point
    try:
        focalFactor = focalLength / (focalLength + z)
    except:
        focalFactor = focalLength / (focalLength + z + 1)
    newX = screenwidth / 2 + x * focalFactor
    newY = screenHeight / 2 - y * focalFactor
    
    return (newX, newY)



def main():
    global focalLength
    running = True
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        for i in range(len(lines)):
            line = lines[i]
            point3d1 = line[0]
            point3d2 = line[1]
            point1 = project(point3d1)
            point2 = project(point3d2)
            # pygame.draw.line(surface, (150, 150, 255), point1, point2, 3)
            pygame.draw.line(surface, lineColours[i], point1, point2, lineWidth)
            
        pygame.display.update()
        
    pygame.quit()



main()