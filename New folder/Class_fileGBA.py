import pygame
from sys import exit
import random
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
       
        super().__init__()
        
        player_fly_1 = pygame.image.load('AlyChar1GBA.png')
        player_fly_2 = pygame.image.load('AlyChar2GBA.png')
        self.player_fly = [player_fly_1, player_fly_2]
        self.player_sprint = pygame.image.load('AlyChar3GBA.png')
        self.player_index = 0
        #player_surf = player_fly[player_index]
        #player_rect = player_surf.get_rect(height = 100, width = 200, topleft = (80,500)) #create player
 
        self.image = self.player_fly[self.player_index]
        self.rect = self.image.get_rect(height = self.image.get_height(), width = self.image.get_width(), topleft = (5,80))
        
        self.xpos = 0
        self.yvel = 0
        #self.sprint_sound = pygame.mixer.Sound('')


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.yvel = -3
        elif keys[pygame.K_DOWN]:
            self.yvel = 3
        else:
            self.yvel = 0
        
        if keys[pygame.K_LEFT]:
            self.xpos -= .2
            if self.xpos >= 10:
                self.xpos = 10
        elif keys[pygame.K_RIGHT]:
            self.xpos += .3
        else: self.xpos -= .125
            

    def movement(self,minvel):
        self.rect.x += self.xpos + minvel
        self.rect.y += self.yvel
        if self.rect.bottom >= 160:
            self.rect.bottom = 160
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= 240:
            self.rect.right = 240
        if self.rect.left <= 5:
            self.rect.left = 5
    
    def animation_state(self):
        keys = pygame.key.get_pressed()
        self.player_index += 0.05
        if keys[pygame.K_RIGHT]:
            self.image = self.player_sprint 
        else:
            if self.player_index >= len(self.player_fly):
                self.player_index = 0
            self.image = self.player_fly[int(self.player_index)]

    
    def update(self,minvel):
        self.player_input()
        self.movement(minvel)
        self.animation_state()




class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        
        super().__init__()
        
        self.type = type
        self.xvel = 0
        self.bonk_image = pygame.image.load('BonkGBA.png').convert_alpha()
        self.collisions = True

        if type == 'pumpkin':
            pump1 = pygame.image.load('pump1GBA.png').convert_alpha()
            pump2 = pygame.image.load('pump2GBA.png').convert_alpha()
            self.frames = [pump1,pump2]
            y_pos = 160
            self.yvel = 0
            self.xvel = 2
            self.animation_inc = .03
        
        elif type == 'bat':
            bat1 = pygame.image.load('Bat1GBA.png').convert_alpha()
            bat2 = pygame.image.load('Bat2GBA.png').convert_alpha()
            self.frames = [bat1,bat2]
            y_pos = 30
            self.yvel = 5*(.5-(random.random()))
            self.xvel = 5
            self.animation_inc = .1

        elif type == 'crow':
            crow1 = pygame.image.load('crow 1.png').convert_alpha()
            crow2 = pygame.image.load('crow 2.png').convert_alpha()
            self.frames = [crow1,crow2]
            y_pos = 30
            self.yvel = 5*(.5-(random.random()))
            self.xvel = 5
            self.animation_inc = .1

        elif type == "crawler":
            crawler1 = pygame.image.load('crawler 1.png').convert_alpha()
            crawler2 = pygame.image.load('crawler 2.png').convert_alpha()
            self.frames = [crawler1,crawler2]
            y_pos = 160
            self.yvel = 0
            self.xvel = 2
            self.animation_inc = .03



        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(280,320),y_pos))
    
    def animation_state(self):
        #self.bonk_image = pygame.image.load('Bonk.png').convert_alpha()
        self.animation_index += self.animation_inc
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        if self.image == self.bonk_image:
            self.image = self.bonk_image
        else:    
            self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.right <= -10:
            self.kill()
    
    def death_animation(self):
        self.image = self.bonk_image
        self.collisions = False

    def update(self):
        self.animation_state()
        self.rect.x -= self.xvel
        self.rect.y += self.yvel
        self.destroy()



class Retrievable(pygame.sprite.Sprite):
    def __init__(self,type):
        
        super().__init__()
        
        self.xvel = 0
        self.type = type
        self.collisions = True
        self.frames = []


        if type == 'book':
            book1 = pygame.image.load('Book1GBA.png').convert_alpha()
            book2 = pygame.image.load('Book2GBA.png').convert_alpha()
            self.frames = [book1, book2]
            y_pos = random.randint(10,130)
            self.yvel = 0
            self.xvel = 2
            self.animation_inc = .08
            self.bonk_image = pygame.image.load('book_bonkGBA.png').convert_alpha()
        
        elif type == 'cat':
            cat1 = pygame.image.load('cat1GBA.png').convert_alpha()
            cat2 = pygame.image.load('cat2GBA.png').convert_alpha()
            self.frames = [cat1, cat2]
            y_pos = 160
            self.yvel = 0
            self.xvel = 4
            self.animation_inc = .05
            self.bonk_image = pygame.image.load('cat_bonkGBA.png').convert_alpha()

        elif type == 'gem':
            gem1 = pygame.image.load('gem 1.png').convert_alpha()
            gem2 = pygame.image.load('gem 2.png').convert_alpha()
            gem3 = pygame.image.load('gem 3.png').convert_alpha()
            
            self.frames = [gem1, gem2, gem3]

            y_pos = 160
            self.yvel = 0
            self.xvel = 3
            self.animation_inc = .05
            self.bonk_image = pygame.image.load('cat_bonkGBA.png').convert_alpha()

        
        elif type == 'potion':
            potion1 = pygame.image.load('potion 1.png').convert_alpha()
            potion2 = pygame.image.load('potion 2.png').convert_alpha()
            potion3 = pygame.image.load('potion 3.png').convert_alpha()
            
            self.frames = [potion1, potion2, potion3]

            y_pos = 160
            self.yvel = 0
            self.xvel = 2
            self.animation_inc = .05
            self.bonk_image = pygame.image.load('book_bonkGBA.png').convert_alpha()

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(250,300),y_pos))

    def animation_state(self):
        #self.bonk_image = pygame.image.load('Bonk.png').convert_alpha()
        self.animation_index += self.animation_inc
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        if self.image == self.bonk_image:
            self.image = self.bonk_image
        else:    
            self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.right <= -10:
            self.kill()
    
    def death_animation(self):
        self.image = self.bonk_image
        self.xvel = .5
        self.yvel = -.5
        self.collisions = False     

    def update(self):
        self.animation_state()
        self.rect.x -= self.xvel
        self.rect.y += self.yvel
        self.destroy()




class Button():
    
    def __init__(self, x, y, image, scale): #add type
        width = image.get_width()
        height = image.get_height()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.x, self.y))

        return action



class Backdrop_Button(pygame.sprite.Sprite):
    
    def __init__(self, type): #add type

        super().__init__()

        self.clicked = False
        self.type = type

        if type == 'lamp':
            lamp1 = pygame.image.load('lamp1GBA.png').convert_alpha()
            lamp2 = pygame.image.load('lamp2GBA.png').convert_alpha()
            self.frames = [lamp1,lamp2]
            y_pos = 160
            self.xvel = 0
            self.animation_inc = .04
            self.bonk_image = pygame.image.load('lamp_bonkGBA.png').convert_alpha()
        
        elif type == 'house':
            house1 = pygame.image.load('House1GBA.png').convert_alpha()
            house2 = pygame.image.load('House2GBA.png').convert_alpha()
            self.frames = [house1,house2]
            y_pos = 160
            self.xvel = 0
            self.animation_inc = .04
            self.bonk_image = pygame.image.load('House_bonkGBA.png').convert_alpha()
        
        elif type == 'portal':
            house1 = pygame.image.load('Portal.png').convert_alpha()
            #house2 = pygame.image.load('House2GBA.png').convert_alpha()
            self.frames = [house1,house1]
            y_pos = 160
            self.xvel = 0
            self.animation_inc = .04
            self.bonk_image = pygame.image.load('Portal.png').convert_alpha()

        elif type == 'bushes':
            bushes1 = pygame.image.load('Bushes.png').convert_alpha()
            #lamp2 = pygame.image.load('lamp2GBA.png').convert_alpha()
            self.frames = [bushes1,bushes1]
            y_pos = 160
            self.xvel = 0
            self.animation_inc = .04
            self.bonk_image = pygame.image.load('bushes.png').convert_alpha()

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(250,300),y_pos))


#    def draw(self, surface):
#
 #       pos = pygame.mouse.get_pos()
#
 #       if self.rect.collidepoint(pos):
  #          if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
   #             self.clicked == True
    #            self.image = self.bonk_image
#
#
 #       if pygame.mouse.get_pressed()[0] == 0:
  #          self.clicked = False
#

    def animation_state(self):
        #self.bonk_image = pygame.image.load('Bonk.png').convert_alpha()
        self.animation_index += self.animation_inc
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True
                self.image = self.bonk_image


        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        if self.image == self.bonk_image:
            self.image = self.bonk_image
        else:    
            self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.right <= -10:
            self.kill()
    
    def update(self):
        self.animation_state()
        #self.draw()
        self.rect.x -= self.xvel
        self.destroy()

