from pygame.locals import *
import pygame
from . import pong

def run_game():
    width = 640
    height = 500
    clock = pygame.time.Clock()
    game = pong.Pong(width,height)
    status = True

    while status:
        clock.tick(64)

        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if pressed[K_ESCAPE]:
                status = False
            if event.type == QUIT:
                status = False

        game.fill()
        game.info()
        game.right_paddle() 
        game.left_paddle()
        game.update_puck()
        pygame.display.flip()
        game.reset()
        pygame.event.pump()
    pygame.quit()