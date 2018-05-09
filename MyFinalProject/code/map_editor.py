import sys
import math
import pygame
from UltraColor import Color
from textures import Tiles

window_width = Tiles.size * 30
window_height = Tiles.size * 20

x_menu = int((int(window_width / Tiles.size) - 6) / 2) * Tiles.size
y_menu = (int(window_height / Tiles.size) - 1) * Tiles.size

window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

def draw_tile(x, y, tile_type):
    window.blit(Tiles.Texture_Defs[tile_type], (x, y))

def draw_tiles_menu():
    x_pos = x_menu
    for tile_type in Tiles.Texture_Defs:
        draw_tile(x_pos, y_menu, tile_type)
        x_pos = x_pos + Tiles.size

def export_map(file):
    map_data = ""

    # Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / Tiles.size)) + "," + str(int(tile[1] / Tiles.size)) + ":" + tile[2] + "-"
        

    # Save Map Dimensions
    map_data = map_data + str(int((max_x / Tiles.size) + 1)) + "," + str(int((max_y / Tiles.size) + 1))


    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)

def import_map(file):
    with open(file, "r") as mapfile:
        map_data = mapfile.read()

    # Read Map Data
    map_data = map_data.split("-")   # Split into list of tiles

    map_size = map_data[len(map_data) - 1]   # Get map dimensions
    map_data.remove(map_size)
    map_size = map_size.split(",")
    map_size[0] = int(map_size[0])
    map_size[1] = int(map_size[1])

    tiles = []

    for tile in range(len(map_data)):
        map_data[tile] = map_data[tile].replace("\n", "")
        tiles.append(map_data[tile].split(":"))   # Split pos from texture

    for tile in tiles:
        tile[0] = tile[0].split(",")   # Split pos into list
        pos = tile[0]
        for p in pos:
            pos[pos.index(p)] = int(p) * Tiles.size   # Convert to integer

        tiles[tiles.index(tile)] = [pos[0], pos[1], tile[1]]   # Save to tile list
    return tiles


txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE | pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0


brush = "5"

map_width = 1 * Tiles.size
map_height = 1 * Tiles.size

# Initialize Default Map
for x in range(0, map_width, Tiles.size):
    for y in range(0, map_height, Tiles.size):
        tile_data.append([x, y, "1"])

isRunning = True


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            if event.key == pygame.K_F4:
                brush = "r"
            elif event.key == pygame.K_F1:
                selection = input("Brush Tag: ")
                brush = selection


            # SAVE MAP
            if event.key == pygame.K_F11:
                name = input("Map Name to Save: ")
                export_map("MyFinalProject\\maps\\" + name + ".map")
                print("Map Saved Successfully!")

            # LOAD MAP
            if event.key == pygame.K_F12:
                name = input("Map Name to Load: ")
                # Read file from disk
                tile_data = import_map("MyFinalProject\\maps\\" + name + ".map")
                print("Map Loaded Successfully!")


        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.size) * Tiles.size
            mouse_y = math.floor(mouse_pos[1] / Tiles.size) * Tiles.size

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_y == y_menu and mouse_x >= x_menu and mouse_x <= x_menu + 6 * Tiles.size:
                # Clicked on menu
                brush = str(int((mouse_x - x_menu) / Tiles.size))
                if brush == '0':
                    brush = 'r'
            else:
                tile = [mouse_x - camera_x, mouse_y - camera_y, brush]   # Keep this as a list

                # Is a tile already placed here?
                found = False
                for t in tile_data:
                    if t[0] == tile[0] and t[1] == tile[1]:
                        found = True
                        break

                # If this tile space is empty
                if not found:
                    if not brush == "r":
                        tile_data.append(tile)

                # If this tile space is not empty
                else:
                    # Are we using the rubber tool?
                    if brush == "r":
                        # Remove Tile
                        for t in tile_data:
                            if t[0] == tile[0] and t[1] == tile[1]:
                                tile_data.remove(t)
                                print("Tile Removed!")

                    else:
                        # Sorry! A tile is already placed here!
                        print("A tile is already placed here!")
                            



    # LOGIC
    if camera_move == 1:
        camera_y += Tiles.size
    elif camera_move == 2:
        camera_y -= Tiles.size
    elif camera_move == 3:
        camera_x += Tiles.size
    elif camera_move == 4:
        camera_x -= Tiles.size



    # RENDER GRAPHICS

    window.fill(Color.Blue)


    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.Texture_Defs[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    draw_tiles_menu()

    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))
    
    

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
