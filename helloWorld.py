#!/usr/bin/env python

#background_image_filename = 'sushiplate.jpg'
from statistics import mode

background_image_filename = 'DSCN00472.JPG'
mouse_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
#from import curses

pygame.init()

screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
pygame.display.set_caption("Hello, World!")
#stdscr=curses.initscr()
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
x2=0
y2=0
while True:
    z=1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        z+=1
#        stdscr.print(0,0,z)
#        if screen.mode() != pygame.display.set_mode((640, 480), RESIZABLE, 32):
        screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
        screen.blit(background, (0,0))

        x, y = pygame.mouse.get_pos()
        x-= mouse_cursor.get_width() / 2
        y-= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))


        pygame.display.update()

