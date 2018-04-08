import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
SCREEN_SIZE = (640, 480)
message="    This is a demonstration of the scrolly message script. "

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

font = pygame.font.SysFont("arial", 80);
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y = ( SCREEN_SIZE[1] - text_surface.get_height() ) / 2

background = pygame.image.load(background_image_filename).convert()

paceMe=False
pacer=0
paceInterval=0

while True:
    pacer+=1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if (event.type == KEYDOWN):
            if event.key == K_p:
                paceMe=True
                paceInterval=200
            elif event.key == K_s:
                paceMe=True
                paceInterval=2000
            else:
                paceMe=False

    screen.blit(background, (0,0))

    x-= 2
    if x < -text_surface.get_width():
        x = 0

    if paceMe:
        if pacer>=paceInterval:
            screen.blit(text_surface, (x, y))
            screen.blit(text_surface, (x+text_surface.get_width(), y))
            pygame.display.update()
            pacer=0
    else:
        screen.blit(text_surface, (x, y))
        screen.blit(text_surface, (x+text_surface.get_width(), y))
        pygame.display.update()