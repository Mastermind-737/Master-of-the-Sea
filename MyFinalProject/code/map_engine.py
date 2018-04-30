import pygame
from main.textures import *
from main.Globals import *

class MapEngine():


    @staticmethod
    def dec_map(map_data):
        dimensones = (0,0)
        ty = 0
        map_datad = []
        for i in map_data:
            i = i.replace("\n","")
            i = i.replace(" ", "")
            map_datax = i.split(";")
            tx = 0
            for i in map_datax:
                xdata = i.split(",")
                if not xdata[1].endswith("$"):
                    map_datad.append((tx + 1,ty,xdata[0], int(xdata[1])))
                    tx += int(xdata[1])
                else:
                    xdata[1] = xdata[1].replace("$","")
                    dimensones = [int(xdata[0]),int(xdata[1])]
            ty += 1

        decoded_map = []
        for i in map_datad:
            for x in range(int(i[3])):
                    decoded_map.append((i[0] + x, i[1], i[2]))

        return decoded_map , dimensones

    @staticmethod
    def add_tile(Texture,x,y,Terrain):
        Terrain.blit(Texture,(x * Tiles.Size ,y * Tiles.Size))


    @staticmethod
    def load_map(file):
        mapdata = open(file,mode="r").readlines()
        map_data = MapEngine.dec_map(mapdata)

        map_size = [map_data[1]]
        map_data = list(map_data)[:-1]

        map_size[0][0] *= Tiles.Size
        map_size[0][1] *= Tiles.Size


        #gen Terrain

        Terrain = pygame.Surface(map_size[0],pygame.HWSURFACE|pygame.SRCALPHA)

        for tile in map_data[0]:
            if tile[2] in Tiles.Texture_Tags:
                MapEngine.add_tile(Tiles.Texture_Tags[tile[2]],tile[0],tile[1],Terrain)
            else:
                print("Tile : "  + str(tile[2]) + "is not a Valid Tile type !")

        return Terrain