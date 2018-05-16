import pygame
from tiles import Tiles

class Map_Loader:

    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.size, pos[1] * Tiles.size))


    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        # Read Map Data
        # Split into list of tiles
        map_data = map_data.split("-")   
        
        # Get map dimensions
        map_size = map_data[len(map_data) - 1]   
        map_data.remove(map_size)
        map_size = map_size.split(",")
        tiles_horizontal = int(map_size[0])
        tiles_vertical = int(map_size[1])
        map_size[0] = tiles_horizontal * Tiles.size
        map_size[1] = tiles_vertical * Tiles.size

        tiles = []
        tiles_array = [[0 for x in range(tiles_horizontal)] for y in range(tiles_vertical)] 

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            # Split pos from texture
            tiles.append(map_data[tile].split(":"))

        for tile in tiles:
            # Split pos into list
            tile[0] = tile[0].split(",")
            pos = tile[0]
            for p in pos:
                # Convert to integer
                pos[pos.index(p)] = int(p)
            # Save to tile list
            tiles[tiles.index(tile)] = (pos, tile[1])
            tiles_array[pos[0]][pos[1]] = tile[1]


        # Create Terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.Texture_Defs:
                Map_Loader.add_tile(Tiles.Texture_Defs[tile[1]], tile[0], terrain)



        return terrain, tiles_array