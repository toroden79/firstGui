import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
screen_width = 640
screen_height = 480
SCREEN_SIZE = (screen_width, screen_height)
#message="    This is a demonstration of the scrolly message script. "
message="This is a demonstration of the scrolly message script."

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

font = pygame.font.SysFont("arial", 80);
text_surface = font.render(message, True, (0, 0, 255))

#x = 0
#y = ( SCREEN_SIZE[1] - text_surface.get_height() ) / 2

#total_x = text_surface.get_width() + screen_width
#total_y = text_surface.get_height() + screen_height
message_width = text_surface.get_width()
message_height = text_surface.get_height()
x=message_width
y=message_height

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
                paceInterval=100
            elif event.key == K_s:
                paceMe=True
                paceInterval=200
            else:
                paceMe=False

    screen.blit(background, (0,0))



    if paceMe:
        if pacer>=paceInterval or x < -message_width or y < -message_height:
            x -= 5
            y -= 2
            if x < -message_width or y < -message_height:
                # x = 0
                x = screen_width
                y = screen_height
            screen.blit(text_surface, (x, y))
            #screen.blit(text_surface, (x+text_surface.get_width(), y))
            pygame.display.update()
            pacer=0
    else:
        x -= 5
        y -= 2
        if x < -message_width or y < -message_height:
            # x = 0
            x = screen_width
            y = screen_height
        screen.blit(text_surface, (x, y))
        #screen.blit(text_surface, (x+text_surface.get_width(), y))
        pygame.display.update()