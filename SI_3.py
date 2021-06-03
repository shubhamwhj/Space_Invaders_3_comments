"""
Spyder Editor

This is a temporary script file.
"""

#getting imprtant libraries
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

#creating the screen where everting will be displayed
screen = pygame.display.set_mode((400,600))

#creating objects of game (player, emeny ships)
player=pygame.Rect(200,500,30,30)
playerSpeed=20
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;

#game loop
while True:    
    screen.fill((0,0,0))  #making the screen background black
    #handling various events such as key press and mouse click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -=playerSpeed
            if event.key ==pygame.K_RIGHT:
                player.x +=playerSpeed
    
    #maving the enemy at x axis
    enemy.x= enemy.x + enemyspeed
    
    #changing enemyspeed to positive or negative on raching the edge of screen.
    #making enemy go to right
    if enemy.x == 0:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    #making enemy go to left
    if enemy.x == 380:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    #drawing the characters on screen       
    pygame.draw.rect(screen,(123,200,100),enemy)
    pygame.draw.rect(screen,(23,100,100),player)
    
    #updating pygame and setting clock to control frame rate/ rate of refreshing the screen.
    pygame.display.update()
    clock.tick(30)

