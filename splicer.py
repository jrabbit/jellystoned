#Source: http://shinylittlething.com/2009/07/21/pygame-and-animated-sprites/
#Using this until it can be rewritten or removed.
import os, sys
import pygame
from pygame.locals import *
from helpers import *

def load_sliced_sprites(w, h, filename):
    '''
    Specs :
    	Master can be any height.
    	Sprites frames width must be the same width
    	Master width must be len(frames)*frame.width
    '''
    images = []
    master_image = load_image(filename, -1)

    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_width/w)):
    	images.append(master_image.subsurface((i*w,0,w,h)))
    return images