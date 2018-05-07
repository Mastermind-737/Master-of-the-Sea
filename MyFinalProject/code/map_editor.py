import pygame, sys, math
from UltraColor import *
from textures import *



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



window = pygame.display.set_mode((700, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()


txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 1 * Tiles.size, 1 * Tiles.size


selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0


brush = "5"



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
                name = input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully!")
            

        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.size) * Tiles.size
            mouse_y = math.floor(mouse_pos[1] / Tiles.size) * Tiles.size

        if event.type == pygame.MOUSEBUTTONDOWN:
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


    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))
    
    

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
