import pygame, sys
from pygame.locals import *
from pygame.math import *

# display dimensions
HEIGHT = 960
WIDTH = 1280

# frames per second
FPS = 60

# radius
R = 50

# bounce factor
BOUNCE = 0.85

pygame.init()
 
clock = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ballaballa")


ball = pygame.image.load("balla.png")


# position
pos = Vector2(WIDTH / 2.0, 200)

# velocity
vel = Vector2(0.0, 0.0)

# acceleration
acc = Vector2(0.0, 0.3)

 
while True:

    #### READ INPUT ###

    # read mouse position
    mousePos = pygame.mouse.get_pos()

    # check user events
    for event in pygame.event.get():

        # mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            impulse = mousePos - pos
            vel += impulse * 0.07

        # exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #### UPDATE ###

    # accelerate
    vel += acc

    # move
    pos += vel


    # check wall collision (x)
    if pos.x - R < 0:
        # left
        pos.x = R
        vel.x = -vel.x * BOUNCE
        vel.y = vel.y * BOUNCE
    elif pos.x + R > WIDTH:
        # right
        pos.x = WIDTH - R
        vel.x = -vel.x * BOUNCE
        vel.y = vel.y * BOUNCE

    # check wall collision (y)
    if pos.y - R < 0:
        # top
        pos.y = R
        vel.y = - vel.y * BOUNCE
        vel.x = vel.x * BOUNCE
    elif pos.y + R > HEIGHT:
        # bottom
        pos.y = HEIGHT - R
        vel.y = - vel.y * BOUNCE
        vel.x = vel.x * BOUNCE


    #### DRAW ###

    # black background
    displaysurface.fill((0,0,0))

    # mouse circle
    pygame.draw.circle(displaysurface, (55,55,55), mousePos, 33)

    # draw ball
    displaysurface.blit(ball, pos - Vector2(R, R))

    # draw velocity line
    pygame.draw.line(displaysurface, (0,200,50), pos, pos + (vel * 10), 3)


    pygame.display.update()
    
    clock.tick(FPS)