import pygame
import math
import random


# create color constans
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [GREEN, RED, BLACK, BLUE]

# create math constants
PI = math.pi

# to convert from degrees to radians angle * (pi / 180)
# 60* pi /180 = pi / 3

# game constants
SIZE = (700, 500)   # width, height
FPS = 60            # frames per second

################################################################################
################################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My First Pygame")

clock = pygame.time.Clock()

running = True

while running:

    # get all keyboard, mouse, controller events
    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("you pressed a key")
        elif event.type == pygame.KEYUP:
            print("you released a key")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("you pressed a mouse button")

    # game logic goes here(objects fried, object movement) goes here

    screen.fill(WHITE)

    # add drawings here
    # pygame.draw.rect(screen, RED, [55, 50, 20, 250], border_radius = 5)
    pygame.draw.arc(screen, BLUE, [55, 50, 200, 200], 0, 5*PI/4, width = 5)

    for multiplier in range(10):
        color = random.choice(COLORS)
        pygame.draw.line(screen, color, (10 + 15*multiplier, 10), (50 + 15*multiplier, 50), 5)

    pygame.display.flip()


    clock.tick(FPS)


# to b run after the main game loop
pygame.quit()
