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
bright_red = (255,0,0)
bright_green = (0,255,0)
red = (200,0,0)
green = (0,200,0)

pause = False

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
  
def quitGame():
    pygame.quit()
    quit()
    
def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
# =============================================================================
#             if(action == "play"):
#                 game_loop()
#             elif action == "quit":
#                 pygame.quit()
#                 quit()     
# =============================================================================
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
        
    small_text = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, small_text)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def unpause():
    global pause
    pause = False

def game_pause():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Paused",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("QUIT",550,450,100,50,red,bright_red,quitGame)
        
        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True 
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Avoid the blocks",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red,bright_red,quitGame)
        
        pygame.display.update()
        clock.tick(15)

#main game loop
def game_loop():
    global pause
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
                elif event.key == pygame.K_p:
                    pause = True
                    game_pause()
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

game_intro()
game_loop() 
pygame.quit()
quit()