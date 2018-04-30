import pygame
pygame.init()

#places graphics on screen in 32,32 squares
class Tiles:
    size = 32
    def load_Texture(file,size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(size, size))
        surface = pygame.Surface((size,size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface
#loads graphics for game
    Grass = load_Texture("MyFinalProject\\Graphics\\World_Assets\\grass.png", size)
    Stone = load_Texture("MyFinalProject\\Graphics\\World_Assets\\stone_brick.jpg", size)
    Water = load_Texture("MyFinalProject\\Graphics\\World_Assets\\water.jpg", size)
    Texture_Defs = {"1" : Grass, "2" : Stone, "3" : Water}