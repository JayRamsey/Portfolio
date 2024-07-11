import pygame
import sys

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GRID_SIZE_SPACES = 10
GRID_SPACE_SIZE = 35
GRID_SIZE_PIXELS = GRID_SPACE_SIZE * GRID_SIZE_SPACES

phase = 0

class square:
    def __init__(self, x, y, w, h, surface, colour, makeButton, tag, command):
        self.shape = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.surface = surface
        self.colour = colour

        if makeButton:
            self.button = button(self, tag, command)
        else:
            self.button = None
            
    def update(self):
        if self.button is not None:
            self.button.draw()
        else:
            self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.shape)

class button:
    def __init_(self, parent, tag, command):
        self.command = command
        self.parent = parent
        self.tag = tag 
        self.rect = parent.shape
        self.x = parent.x
        self.y = parent.y
        self.width = parent.width
        self.height = parent.height

    def draw(self):
        self.parent.draw()

    def clicked(self):
        self.command()
        
def helloworld():
    print("Hello World")
    
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

playerGrid = pygame.Surface((GRID_SIZE_PIXELS, GRID_SIZE_PIXELS))
playerGrid.fill((255, 255, 255))

mySquare = square(0, 0, GRID_SPACE_SIZE, GRID_SPACE_SIZE, playerGrid, (0, 0, 255), True, "my button", helloworld)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if phase == 0:
                pass

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mySquare.update()
    
    screen.blit(playerGrid, (30, 30))
    pygame.display.update()
    
    clock.tick(60)
