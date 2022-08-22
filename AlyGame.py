#use the dummy video driver from os
#import os
#os.environ["SDL_VIDEODRIVER"] = 'dummy'
#os.environ['SDL_AUDIODRIVER'] = 'dsp'

#Using the pygame module to get started
import pygame
import math
from pygame.locals import*
#import system access
import sys
import random
import Class_file
#import numpy as np



#def display_score(score_books = 0, score_cats = 0):
#    score_time = pygame.time.get_ticks()
#    score_text = font.render(f"Books = {score_books}     Cats = {score_cats}    Time = {score_time}", False, 'Purple')
#    score_rect = score_text.get_rect(center = (576,100))


#define the main function
def game_main():


  

    #initialize the pygame module
    pygame.init()



    # Sprite Groups
    # players
    player_2 = pygame.sprite.GroupSingle()
    player_2.add(Class_file.Player())

    # obstacles
    obstacles = pygame.sprite.Group()
   
    #obstacles.add() event setup
    OBSTACLE_TIMER_1 = pygame.USEREVENT + 1
    OBSTACLE_TIMER_2 = pygame.USEREVENT + 2
    pygame.time.set_timer(OBSTACLE_TIMER_1, 3000)
    pygame.time.set_timer(OBSTACLE_TIMER_2, 5000)



    #Name of the game
    pygame.display.set_caption("Saving Samhain")

    #color palette
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)



    #create a surface on screen that has a given m x n pixel size
    screen_width = 1152 #background size
    screen_length = 648 #background size
    screen = pygame.display.set_mode((screen_width, screen_length))
    #screen = pygame.display.set_mode((240, 180)) #what the demo uses
    
    #text setup
    #font Setting
    textX = 400
    textY = 400
    font = pygame.font.Font('freesansbold.ttf', 32)
    pause_text = font.render('Paused', True, green, blue)
    pause_textRect = pause_text.get_rect()
    pause_textRect.center = (textX // 2, textY // 2)




    #collision objects
    collision_text = pygame.image.load('Ouch.png').convert_alpha()
    collision_textRect = collision_text.get_rect(center = (576,324))
    bonk_surf = pygame.image.load('Bonk.png').convert_alpha()
    bonk_rect = bonk_surf.get_rect(center = (0,0))


    #level up object
    level_up_surf = pygame.image.load("Level_up.png").convert_alpha()
    level_up_rect = level_up_surf.get_rect(center = (576, 300))


    score_books = 0
    score_cats = 0
    bonks = 0
    score_time = pygame.time.get_ticks()
    
    #title_text = font
    score_text = font.render(f"Books = {score_books}     Cats = {score_cats}     Time = {score_time//1000}", False, 'Purple')
    score_rect = score_text.get_rect(center = (576,100))
    #scoreDisp = pygame.Surface((400,200))#
    #pygame.font.render(screen,'Black',score_rect,border_radius=2)



    # Background
    #Background surface: size = 1152 x 648
    background_surface = pygame.image.load('AlyGameBackGround.png').convert()#convert speeds this up

    #House object for animation: size = 500 x 500
    houseOne_surface = pygame.image.load('House1.png').convert_alpha()#only convert background
    houseOne_rect = houseOne_surface.get_rect(midbottom = (1000,648))
    #house_x = 1000 #initial x position = 1000 - 500 = 500
    
    #lamp objects
    lamp1_surf = pygame.image.load('lamp.png').convert_alpha()
    lamp1_rect = lamp1_surf.get_rect(midbottom = (1152,665))
    lamp2_surf = pygame.image.load('lamp.png').convert_alpha()
    lamp2_rect = lamp2_surf.get_rect(midbottom = (395,665))



    # Retrievables
    #book objects
    book_surf = pygame.image.load('Book.png').convert_alpha()
    book_rect = book_surf.get_rect(center = (1300, random.randint(0,600)))
    book_rect.inflate(-30,-30)

    #cat objects
    cat_surf = pygame.image.load('kitty.png').convert_alpha()
    cat_rect = cat_surf.get_rect(midbottom = (2000, 665))



    #Obstacles
    #pumpkin objects
    pump1_surf = pygame.image.load('pumpkin2.png').convert_alpha()
    pump1_rect = pump1_surf.get_rect(midbottom = (1300,665))
    #pump1_rect.inflate(150,-50)

    #bat objects
    bat_surf = pygame.image.load('bat.png').convert_alpha()
    bat_rect = bat_surf.get_rect(midbottom = (1500, random.randint(100,400)))



    #character surface
    player_fly_1 = pygame.image.load('AlyCharacter1.png')
    player_fly_2 = pygame.image.load('AlyCharacter2.png')#.convert()
    player_fly = [player_fly_1, player_fly_2]
    player_index = 0
    player_sprint = pygame.image.load('AlyCharacter3.png')

    player_surf = player_fly[player_index]
    player_rect = player_surf.get_rect(height = 100, width = 200, topleft = (80,500)) #create player
    
    #player_rect.inflate(400,-400)
    player_yvel = 0
    player_xvel = 0
    #object box/rectangle



    #testing out the blit function: blit(imagename,location)
    #screen.blit(logo, (50,50))
    pygame.display.flip()
    
    # define the position of the logo
    xpos = 200
    ypos = 200
    # how many pixels we move the logo each frame
    step_x = 10
    step_y = 10

    #define a variable to control the main loop
    running = True #needs a Boolean argument to run the loop

    #Create a clock object to set framerate
    clock = pygame.time.Clock()
    timer = 0

    maxvel = 10
    minvel = 1
    game_active = True 



    # main loop
    while running: #infinite loop
       
        current_time = ...
        button_press_time = ...



        #reset motion mechanics
        #player_yvel = 0





        #event handling, gets all events from the event queue
        for event in pygame.event.get():

            #Game Exit
            if event.type == pygame.QUIT:

                #change the calue to False, exit the infinite loop
                running = False
                #sys.exit()


            #Obstacle timer constructions
            if event.type == OBSTACLE_TIMER_1:
                obstacles.add(Class_file.Obstacle('pumpkin'))
            
            if event.type == OBSTACLE_TIMER_2:
                obstacles.add(Class_file.Obstacle('bat'))


            #Active game commands
            if game_active:

                if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_SPACE:
                    if event.key == pygame.K_UP:
                        player_yvel = -12
                    elif event.key == pygame.K_DOWN:
                        player_yvel = 12
                    
                    if event.key == pygame.K_RIGHT:
                        if player_xvel >= 10:
                            player_xvel = 10
                        else: player_xvel += 2

                    elif event.key == pygame.K_LEFT:
                        if player_xvel <= 0:
                            player_xvel = 0
                        else: player_xvel -= 2 




                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_yvel = 0
                
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        pump1_rect.left = 1200
                        bat_rect.left = 1300

                            
                


        if game_active:
            #display objects in order from back to front
            #display_score(score_text = )
            screen.blit(background_surface,(0,0))
            screen.blit(houseOne_surface,houseOne_rect) #0, LENGTH - HOUSE HEIGHT
            screen.blit(lamp1_surf,lamp1_rect)
            screen.blit(lamp2_surf, lamp2_rect)
            #player_animation()
            #screen.blit(player_surf,player_rect)
            player_2.draw(screen)
            player_2.update()
            obstacles.draw(screen)
            obstacles.update()
            pygame.draw.rect(screen,'Grey',score_rect,width = 2,border_radius=5)
            screen.blit(score_text, score_rect)
            screen.blit(book_surf, book_rect)
            #screen.blit(pump1_surf,pump1_rect)
            #screen.blit(bat_surf,bat_rect)
            screen.blit(cat_surf, cat_rect)
            score_time = pygame.time.get_ticks()//1000
            score_text = font.render(f"Books: {score_books}     Cats: {score_cats}     Time: {score_time}", False, 'Purple')
            score_rect = score_text.get_rect(center = (576,100))

            
            # Level completion
            total_score = score_books*5 + score_cats*20 + score_time
            if total_score >= 200:
                #end of game animation:
                pygame.time.wait(1000)
                screen.blit(level_up_surf, level_up_rect)
                pygame.time.wait(1000)
                score_text = font.render(f"Books = {score_books}     Cats = {score_cats}     Time = {score_time//1000}", False, 'Black')
                score_rect = score_text.get_rect(center = (576,600))
                screen.blit(score_text,score_rect)
                pygame.time.wait(1000)
                game_active = False
                #continue

            #animated portion of background
            houseOne_rect.x -= (player_xvel + minvel)
            if houseOne_rect.right < -350:
                houseOne_rect.left = 1100 #loop the house position
            
            lamp1_rect.x -= (7/5)*(player_xvel + minvel)
            if lamp1_rect.right < -200:
                lamp1_rect.left = 1200
            
            lamp2_rect.x -= (7/5)*(player_xvel + minvel)
            if lamp2_rect.right < -200:
                lamp2_rect.left = 1200

            book_rect.x -= (3/5)*(player_xvel + minvel)
            if book_rect.right < -400:
                book_rect.left = 1200
                book_rect.bottom = random.randint(50,600)

            cat_rect.x -= 2*(player_xvel + minvel)
            if cat_rect.right < -400:
                cat_rect.left = 4800

            pump1_rect.x -= (player_xvel + minvel)
            if pump1_rect.right < -100:
                pump1_rect.left = 1300

            bat_rect.x -= (6/5)*(player_xvel + minvel)
            bat_rect.y = 100*math.sin(pygame.time.get_ticks()/200) + 50
            if bat_rect.right < -100:
                bat_rect.left = 1400
            
            #game part: collisions and controls
            #print(player_rect.center)
            if player_rect.collidepoint(pump1_rect.center): #or player_rect.colliderect(lamp2_rect):
                #screen.blit(collision_animation,collisionRectangle)
                screen.blit(collision_text, collision_textRect)
                bonk_rect = bonk_surf.get_rect(center = pump1_rect.center)
                screen.blit(bonk_surf, bonk_rect)
                bonks += 1
                total_score -= 5 #pumpkin collision score modifier
                pygame.display.update()
                pygame.time.wait(250)
                game_active = False
            
            if player_rect.collidepoint(bat_rect.center): #or player_rect.colliderect(lamp2_rect):
                #screen.blit(collision_animation,collisionRectangle)
                screen.blit(collision_text, collision_textRect)
                bonk_rect = bonk_surf.get_rect(center = bat_rect.center)
                screen.blit(bonk_surf, bonk_rect)
                bonks += 1
                total_score -= 3 #pumpkin collision score modifier
                pygame.display.update()
                pygame.time.wait(250)
                game_active = False

            if player_rect.collidepoint(book_rect.center):
                score_books += 1
                book_rect.x = 2000
                book_rect.bottom = random.randint(50,600)
                score_text = font.render(f"Books: {score_books}     Cats: {score_cats}     Time: {score_time}", False, 'Purple')
                score_rect = score_text.get_rect(center = (576,100))
                #screen.blit(book name and image)

            if player_rect.collidepoint(cat_rect.center):
                score_cats += 1
                cat_rect.x = 2000
                score_text = font.render(f"Books: {score_books}     Cats: {score_cats}     Time: {score_time}", False, 'Purple')    
                score_rect = score_text.get_rect(center = (576,100))
            

            if player_rect.bottom >= 648:
                player_rect.bottom = 648
            if player_rect.top <= 0:
                player_rect.top = 0

            #player_yvel += player_yaccel
            player_rect.y += player_yvel

            minvel = 2*(score_time//10 + 1)
            maxvel = 2*(score_time//10 + 10)

            #book score
            #if 
                
    
            pygame.display.update()
            #step time at 60fps
            clock.tick(60)

            #if spider_rect.colliderect(player_rect):
                #game_active = False

#Run the main function only if this module is the main script
# so if it is imported, nothing happens unless the function is called
if __name__ == "__main__":
    game_main()
        
