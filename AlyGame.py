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


    #retrievables
    retrievables = pygame.sprite.Group()
    OBSTACLE_TIMER_3 = pygame.USEREVENT + 3
    pygame.time.set_timer(OBSTACLE_TIMER_3, 6500)

    

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


    #pause menu
    menu_font = pygame.font.SysFont("arial", 40)
    
    def pause_text(text,font,text_col,x,y):
        img = font.render(text, True, text_col)
        #game_active = False
        screen.fill((0,205,0))
        screen.blit(img, (x,y))
        pygame.display.flip()
        


    #Home screen items
    #play button
    play_button = Class_file.Button(575,375,pygame.image.load("play_button.png").convert_alpha(),1)
    title_men1 = pygame.image.load("title_text_1.png").convert_alpha()
    title_men1_rect = title_men1.get_rect(topleft = (3,25))
    title_men2 = pygame.image.load("title_text_2.png").convert_alpha()
    title_men2_rect = title_men2.get_rect(topleft = (425,220))
    control_men = pygame.image.load("Home_controls_and_values.png").convert_alpha()
    control_men_rect = control_men.get_rect(topleft = (3, 250))





    #collision objects
    collision_text = pygame.image.load('Ouch.png').convert_alpha()
    collision_textRect = collision_text.get_rect(center = (576,324))
    #bonk_surf = pygame.image.load('Bonk.png').convert_alpha()
    #bonk_rect = bonk_surf.get_rect(center = (0,0))


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

    #game variables
    #idea board:
    # auto to start menu (level 0)
    # go from start menu to level 1
    # etc.
    # If game_paused == 1:
    # game_active = 0, and game_active runs the levels,
    #while game_paused runs the pause function
    game_active = 0 #game key: 0 = open, 1 = pause, 2 = end game, 3 = level 1,... 
    game_paused = False




    # main loop
    while running: #infinite loop
       

        if game_active == 0:

            if game_paused == False:

                screen.blit(title_men1,title_men1_rect)# Title
                screen.blit(title_men2, title_men2_rect)
                screen.blit(control_men, control_men_rect)# controls
                click = play_button.draw(screen)
                if click == True:
                    game_active = True
                pygame.display.flip()
            
            #else:
#
 #               pause_text("Paused", font, (0,0,0), 576, 300) 
  #              game_paused = True
   #             game_active = 0
    #            for event i










        #event handling, gets all events from the event queue
        for event in pygame.event.get():

            #Game Exit
            if event.type == pygame.QUIT:

                #change the calue to False, exit the infinite loop
                running = False
                #sys.exit()


            #Active game commands
            if game_active == 1:

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

                    #elif event.key == pygame.K_p:
                     #   pause_text("Paused", font, (0,0,0), 576, 300) 
                        #game_paused = True
                        #game_active = (game_active + 1)%2  

                                #Obstacle timer constructions
                
                if event.type == OBSTACLE_TIMER_1:
                    obstacles.add(Class_file.Obstacle('pumpkin'))
            
                if event.type == OBSTACLE_TIMER_2:
                    obstacles.add(Class_file.Obstacle('bat'))
            
                if event.type == OBSTACLE_TIMER_3:
                    retrievables.add(Class_file.Retrievable(random.choice(['book', 'book', 'book', 'cat'])))  





                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_yvel = 0
                
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        #pump1_rect.left = 1200
                        #bat_rect.left = 1300

                            
                


        if game_active == 1:
            #display objects in order from back to front
            #display_score(score_text = )
            screen.blit(background_surface,(0,0))
            screen.blit(houseOne_surface,houseOne_rect) #0, LENGTH - HOUSE HEIGHT
            screen.blit(lamp1_surf,lamp1_rect)
            screen.blit(lamp2_surf, lamp2_rect)


            #screen.blit(player_surf,player_rect)  
            player_2.draw(screen)
            player_2.update()

            obstacles.draw(screen)
            obstacles.update()

            retrievables.draw(screen)
            retrievables.update()
            
            
            pygame.draw.rect(screen,'Grey',score_rect,width = 2,border_radius=5)
            score_time = pygame.time.get_ticks()//1000
            score_text = font.render(f"Books: {score_books}     Cats: {score_cats}     Time: {score_time}", False, 'Purple')
            score_rect = score_text.get_rect(center = (576,100))
            screen.blit(score_text, score_rect)
            
            #update scores
            score_time = pygame.time.get_ticks()//1000
            #score_text = font.render(f"Books: {score_books}     Cats: {score_cats}     Time: {score_time}", False, 'Purple')
            #score_rect = score_text.get_rect(center = (576,100))

            
            # Level completion
            total_score = score_books*5 + score_cats*20 + score_time
            if total_score >= 120:
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



           

            minvel = 2*(score_time//10 + 1)
            maxvel = 2*(score_time//10 + 10)
            
            for ret in retrievables:
                ret.xvel += minvel/50
            for obs in obstacles:
                obs.xvel += minvel/50

            #book score
            #if 
                
    
            pygame.display.update()
            #step time at 60fps
            clock.tick(60)
            
            wrecks = pygame.sprite.spritecollide(player_2.sprite, obstacles, False)
            if wrecks != []:
                if wrecks[0].collisions == True:
                    bonks += 1
                wrecks[0].death_animation()
                if (bonks%3) == 0:
                    screen.blit(collision_text, collision_textRect)
                    pygame.display.update()
                    pygame.time.wait(250)
                    wrecks[0].kill()
                # add lives here

            retrievals = pygame.sprite.spritecollide(player_2.sprite, retrievables, False)
            if retrievals != []:
                if retrievals[0].type == 'book' and retrievals[0].collisions == True:
                    score_books += 1
                elif retrievals[0].type == 'cat' and retrievals[0].collisions == True:
                    score_cats += 1
                retrievals[0].death_animation()



#Run the main function only if this module is the main script
# so if it is imported, nothing happens unless the function is called
if __name__ == "__main__":
    game_main()
        
