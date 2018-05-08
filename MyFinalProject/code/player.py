import pygame
from NPC import *

pygame.init()

class Player:
    def ___init__(self,name):
        self.name = name
        self.facing = "south"
        self.health = 100
        sprite = pygame.image.load("MyFinalProject\\Graphics\\Character_Assets\\playerdemo.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]

        #Get player faces (front,back,left,right)
        self.faces = get_faces(sprite)

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing],pos)
