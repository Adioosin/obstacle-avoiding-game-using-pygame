# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:42:06 2018

@author: guest11
"""

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Racey')

clock = pygame.time.Clock()

crashed = False

while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()    
    