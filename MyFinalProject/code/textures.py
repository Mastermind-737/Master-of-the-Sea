import pygame


#places graphics on screen in 32,32 squares
class Tiles:
    
    size = 32
    
    Blocked = []

    Blocked_types = ["3","2","5"]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False

    def load_Texture(file,size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(size, size))
        surface = pygame.Surface((size,size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface
#loads graphics for game
    Delete = load_Texture("MyFinalProject\\Graphics\\World_Assets\\delete.png", size)
    Grass = load_Texture("MyFinalProject\\Graphics\\World_Assets\\grass.png", size)
    Stone = load_Texture("MyFinalProject\\Graphics\\World_Assets\\stone_brick.jpg", size)
    Water = load_Texture("MyFinalProject\\Graphics\\World_Assets\\water.jpg", size)
    Sand = load_Texture("MyFinalProject\\Graphics\\World_Assets\\sand.jpg", size)
    Wood = load_Texture("MyFinalProject\\Graphics\\World_Assets\\wood.jpg", size)
    Texture_Defs = {"0" : Delete, "1" : Grass, "2" : Stone, "3" : Water, "4" : Sand, "5" : Wood}