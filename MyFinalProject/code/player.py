# Imports pygame
import pygame

def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_width = int(size[0]/2)
    tile_height = int(size[1]/2)
    tile_size = (tile_width, tile_height)

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0, 0, tile_width, tile_height))
    faces["south"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_width, tile_height, tile_width, tile_height))
    faces["north"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_width, 0, tile_width, tile_height))
    faces["east"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_height, tile_width, tile_height))
    faces["west"] = west

    return faces

class Player:
    def __init__(self, name):
        self.name = name
        self.facing = "south"
        sprite = pygame.image.load("MyFinalProject\\Graphics\\Character_Assets\\playerdemo.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]

        #Get player faces (front,back,left,right)
        self.faces = get_faces(sprite)

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing],pos)


