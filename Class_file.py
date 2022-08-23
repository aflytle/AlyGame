import pygame
from sys import exit
import random
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
       
        super().__init__()
        
        player_fly_1 = pygame.image.load('AlyCharacter1.png')
        player_fly_2 = pygame.image.load('AlyCharacter2.png')
        self.player_fly = [player_fly_1, player_fly_2]
        self.player_sprint = pygame.image.load('AlyCharacter3.png')
        self.player_index = 0
        #player_surf = player_fly[player_index]
        #player_rect = player_surf.get_rect(height = 100, width = 200, topleft = (80,500)) #create player
 
        self.image = self.player_fly[self.player_index]
        self.rect = self.image.get_rect(height = 100, width = 200, topleft = (80,500))
        
        self.xpos = 0
        self.yvel = 0
        #self.sprint_sound = pygame.mixer.Sound('')


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.yvel = -12
        elif keys[pygame.K_DOWN]:
            self.yvel = 12
        else:
            self.yvel = 0
        
        if keys[pygame.K_LEFT]:
            self.xpos -= .2
            if self.xpos >= 10:
                self.xpos = 10
        elif keys[pygame.K_RIGHT]:
            self.xpos += .5
        else: self.xpos -= .25
            

    def movement(self):
        self.rect.x += self.xpos
        self.rect.y += self.yvel
        if self.rect.bottom >= 648:
            self.rect.bottom = 648
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= 1100:
            self.rect.right = 1100
        if self.rect.left <= 80:
            self.rect.left = 80
    
    def animation_state(self):
        keys = pygame.key.get_pressed()
        self.player_index += 0.05
        if keys[pygame.K_RIGHT]:
            self.image = self.player_sprint 
        else:
            if self.player_index >= len(self.player_fly):
                self.player_index = 0
            self.image = self.player_fly[int(self.player_index)]

    
    def update(self):
        self.player_input()
        self.movement()
        self.animation_state()




class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        
        super().__init__()
        
        self.type = type
        self.xvel = 0
        self.bonk_image = pygame.image.load('Bonk.png').convert_alpha()
        self.collisions = True

        if type == 'pumpkin':
            pump1 = pygame.image.load('pumpkin2.png').convert_alpha()
            pump2 = pygame.image.load('pumpkin3.png').convert_alpha()
            self.frames = [pump1,pump2]
            y_pos = 665
            self.yvel = 0
            self.xvel = 5
            self.animation_inc = .03
        
        else:
            bat1 = pygame.image.load('Bat1.png').convert_alpha()
            bat2 = pygame.image.load('Bat2.png').convert_alpha()
            self.frames = [bat1,bat2]
            y_pos = 300
            self.yvel = 5*(.5-(random.random()))
            self.xvel = 7
            self.animation_inc = .1


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(1200,1400),y_pos))
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
        if self.rect.right <= -100:
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

        if type == 'book':
            book1 = pygame.image.load('Book1.png').convert_alpha()
            book2 = pygame.image.load('Book2.png').convert_alpha()
            self.frames = [book1,book2]
            y_pos = random.randint(50,610)
            self.yvel = 0
            self.xvel = 5
            self.animation_inc = .08
            self.bonk_image = pygame.image.load('book_bonk.png').convert_alpha()
        
        elif type == 'cat':
            cat1 = pygame.image.load('cat1.png').convert_alpha()
            cat2 = pygame.image.load('cat2.png').convert_alpha()
            self.frames = [cat1,cat2]
            y_pos = 652
            self.yvel = 0
            self.xvel = 10
            self.animation_inc = .05
            self.bonk_image = pygame.image.load('cat_bonk.png').convert_alpha()


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(1200,1400),y_pos))

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
        if self.rect.right <= -100:
            self.kill()
    
    def death_animation(self):
        self.image = self.bonk_image
        self.xvel = .5
        self.yvel = -5
        self.collisions = False

        
        

    def update(self):
        self.animation_state()
        self.rect.x -= self.xvel
        self.rect.y += self.yvel
        self.destroy()




class Button():
    
    def __init__(self, x, y, image, scale):
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
