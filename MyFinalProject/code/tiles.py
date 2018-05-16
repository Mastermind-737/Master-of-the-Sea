import pygame


# Places graphics on screen in 32,32 squares
class Tiles:
    
    size = 32

    def is_blocked(tile_type):
        return tile_type in ["2", "3", "5"]

    def load_Texture(file,size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(size, size))
        surface = pygame.Surface((size,size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface
    # Loads graphics for game
    Delete = load_Texture("MyFinalProject\\Graphics\\World_Assets\\delete.png", size)
    Grass = load_Texture("MyFinalProject\\Graphics\\World_Assets\\grass.png", size)
    Stone = load_Texture("MyFinalProject\\Graphics\\World_Assets\\stone_brick.jpg", size)
    Water = load_Texture("MyFinalProject\\Graphics\\World_Assets\\water.jpg", size)
    Sand = load_Texture("MyFinalProject\\Graphics\\World_Assets\\sand.jpg", size)
    Wood = load_Texture("MyFinalProject\\Graphics\\World_Assets\\wood.jpg", size)
    Texture_Defs = {"0" : Delete, "1" : Grass, "2" : Stone, "3" : Water, "4" : Sand, "5" : Wood}