#!/usr/bin/env python
# 2010. Jrabbit. GPL v3 or later.
#Support only offered for Haiku OS
import os, sys
import pygame
import random
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from helpers import *
#boilerplate pygame used lovingly from http://www.learningpython.com/2006/03/12/creating-a-game-in-python-using-pygame-part-one/
class GameMain:
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        pygame.display.set_caption("Jelleystoned! By Jrabbit!", "jellystoned")
        self.screen = pygame.display.set_mode((self.width, self.height))
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        self.load_sprites()
        self.load_music()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.bear.move(event.key)
            self.background = pygame.Surface(self.screen.get_size())
            self.background = self.background.convert()
            self.background.fill((85,98,112))
            self.screen.blit(self.background, (0, 0))
            self.bear_sprites.draw(self.screen)
            self.cop_sprites.draw(self.screen)
            self.cop_sprites.update(pygame.time.get_ticks())
            self.lstCols = pygame.sprite.spritecollide(self.bear, self.cop_sprites, False)
            if self.lstCols:
                print self.lstCols
            pygame.display.flip()
    def load_sprites(self):
        self.bear = Bear()
        self.bear_sprites = pygame.sprite.RenderPlain(self.bear)
        self.cop = Cop()
        self.cop_sprites = pygame.sprite.RenderPlain(self.cop)
    def load_music(self):
        pygame.mixer.music.load(os.path.join('data', 'music', '05 - What would Freud say.ogg'))
        pygame.mixer.music.play()
    

class Cop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fps = 10
        self.image, self.rect = load_image('cop_0.png',-1)
        self.position = (500, random.randint(0,350))
        self.rect.move_ip(self.position)
        self.start = pygame.time.get_ticks()
        self.delay = 1000
        self.run_seq = 0
        self.last_update = 0
    def update(self, t):
        """badies should mofe from right to left."""
        if t - self.last_update > self.delay:
            self.XMove = random.randint(-40,-10)
            self.YMove = 0
            self.run_seq += 1
            self.image , self.rect = load_image('cop_%d.png' % self.run_seq,-1)
            self.move = (self.position[0] + self.XMove, self.position[1] + self.YMove)
            self.position = self.move
            self.last_update = t
            self.rect.move_ip(self.move)
        if self.run_seq >= 9:
            # loop the animation
            self.run_seq = 0


class Bear(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.src_image = pygame.image.load(image)
        self.image, self.rect = load_image('bear.png',-1)
        self.x_dist = 15
        self.y_dist = 15
        #ME GO TOO FAR!
        #self.position = position
        self.speed = self.direction = 0 
        # self.k_left = self.k_right = self.k_down = self.k_up = 0
    def move(self, key):
        xMove = 0
        yMove = 0
        
        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        self.rect.move_ip(xMove,yMove)


if __name__ == "__main__":
    MainWindow = GameMain()
    MainWindow.MainLoop()
