# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 13:50:55 2018

@author: guest11
"""

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
white = (255,255,255)
black = (0,0,0)

car_width = 75
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racey')

clock = pygame.time.Clock()

#png of the car
carImg = pygame.image.load('race_car.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count),True, black)
    gameDisplay.blit(text,(0,0)) #to display on screen

#drawing things using pygame draw function
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y)) #to display on screen
  
# creatig object for the displaying of the messages i.e. surface and rectangle
def text_objects(text, font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()
 
#displaying message on screen
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()

def crash():
    message_display('You Crashed')



#main game loop
def game_loop():
    #placing car on screen
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    
    #initializing things specifications
    thing_width = 100
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -600
    thing_speed = 7
    thing_height = 100
    
    dodged = 0
    
    gameExit = False
    
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #controlling cars movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key ==pygame.K_RIGHT:
                    x_change = 5
            #dont change x if we lift the finger from the key        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        # changing the x-coordinate of car         
        x +=x_change
        
        #Displaying
        #filling screen with white background
        gameDisplay.fill(white)
        #placing things on the screen
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        #changing y-coordinate of things to make it move
        thing_starty += thing_speed
        car(x,y)
        #displaying dodge counter on the top left corner
        things_dodged(dodged)
        
        #setting boundaries for the game
        if x > (display_width-car_width) or x < 0:
            crash()
        #reinitializing things once they are off the screen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width-thing_width)
            dodged += 1
            #thing_speed +=1
            #thing_width += (dodged * 1.2)
            
        #check for the collision with the things
        if y < thing_starty + thing_height: #checking for y
            #checking for x
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()
        #updating the display
        pygame.display.update()
        clock.tick(60)

#game_intro()
game_loop() 
pygame.quit()
quit()