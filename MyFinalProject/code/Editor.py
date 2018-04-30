import pygame, sys, math
from main.UltraCollor import *
from main.textures import *
import main.map_engine



def load_map(file):
    global tile_data , tile_size
    mapdat = open(file,mode="r").readlines()
    mapdat = main.map_engine.MapEngine.dec_map(mapdat)

    map_size = [mapdat[1]]
    mapdat = list(mapdat)[:-1]

    map_size[0][0] *= Tiles.Size
    map_size[0][1] *= Tiles.Size

    tiles = []

    for tile in mapdat[0]:

        tiles.append((int(tile[0] * Tiles.Size), int(tile[1]) * Tiles.Size, str(tile[2])))

    tile_data = tiles

    print("map was Loaed Sucssefully , Dimesions : " + str(map_size[0]) + " Pixels .")

def fill(startpos,endpos,tiletype):

    for y in range(endpos[1]):
        for x in range(endpos[0]):
            #make sure that there is no Tile
            tile_data.append(((x + startpos[0]) * Tiles.Size ,(y + startpos[1]) * Tiles.Size,tiletype))



def ord_list(liste):

    liste = liste

    prev = []

    change = len(liste)

    while not change == 0:

        if change == 0:
            continue

        for i in range(len(liste)):
            x = liste[i][0]
            y = liste[i][1]

            try:
                nx = liste[i + 1][0]
                ny = liste[i + 1][1]

                if y > ny:
                    liste[i], liste[i + 1] = liste[i + 1], liste[i]
                if y == ny:
                    if x > nx:
                        liste[i], liste[i + 1] = liste[i + 1], liste[i]
            except:
                pygame.display.update()
                pass

            if change == 0:
                continue

            if liste == prev:
                change -= 1

            prev = liste

    return liste




def splitline(spliter,linelist):
    questionchunks = []
    qlist = []
    linelist.append('') # append an empty str at the end to avoid the other condn
    for line in linelist:

        if (line != spliter ):
            questionchunks.append(line)      # add the element to each of your chunk
        else:
            qlist.append(questionchunks)   # append chunk
            questionchunks = []       # reset chunk

    return qlist

def liststr_to_list(liste):
    wholelist = []
    for i in liste:
        temp = []
        for b in i:
            b = eval(b)
            temp.append(b)
        wholelist.append(temp)
    return wholelist


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

    #ord map

    tile_dat = ord_list(tile_data)
    print(tile_dat)

    # prepare map Tiles




    t_lenght = len(tile_dat)

    templines = []

    for i in range(t_lenght):
        try:
            if tile_dat[i + 1][1] == tile_dat[i][1]:
                templines.append(str([tile_dat[i][0],tile_dat[i][1],tile_dat[i][2]]))
            else:
                templines.append(str([tile_dat[i][0], tile_dat[i][1], tile_dat[i][2]]))
                templines.append("endline")
        except:
            templines.append(str([tile_dat[i][0], tile_dat[i][1], tile_dat[i][2]]))
            templines.append("endline")

    #print(templines)

    liste = splitline("endline",templines)

    #print(liste[0])

    finish = []

    for v in liststr_to_list(liste):
        t_lenght = len(v)
        liste = []
        totla_lenght = 1
        for tile in range(t_lenght):
            tx = int(v[tile][0] / Tiles.Size)
            nexttx = (tx + 1) * Tiles.Size

            try:
                if nexttx == v[tile + 1][0] and v[tile][2] == v[tile + 1][2]:
                    totla_lenght += 1

                else:
                    liste.append((v[tile][2], totla_lenght))
                    totla_lenght = 1

            except:
                liste.append((v[tile][2], totla_lenght))
                totla_lenght = 1

        finish.append(liste)


    #print(finish)

    #save map tiles

    map_data = []
    for i in finish:
        temp = []
        for b in i:
            cu_len = 0
            templen = len(i)
            if not len(i) == cu_len:
                temp.append(str(b[0]) + "," + str(b[1]) + ";")
            else:
                temp.append(str(b[0]) + "," + str(b[1]))
            cu_len += 1
        map_data.append("".join(temp) + "\n")

    map_data = "".join(map_data)


    # Save Map Dimensions
    map_data = map_data + str(int(max_x / Tiles.Size)) + "," + str(int(max_y / Tiles.Size)) + "$"

    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)



window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * Tiles.Size, 100 * Tiles.Size

selector = pygame.Surface((Tiles.Size, Tiles.Size), pygame.HWSURFACE | pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = "5"


"""""
for y in range(0,map_width, Tiles.Size):
    for x in range(0,map_height,Tiles.Size):
        tile_data.append([x,y,"A"])
"""""


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

            # Fill

            elif event.key == pygame.K_F3:
                start_pos = input("start position : ")

                start_pos = start_pos.replace("/n", "")
                start_pos = start_pos.replace(" ", "")
                start_pos = start_pos.split(",")

                end_pos = input("end position : ")

                end_pos = end_pos.replace("/n", "")
                end_pos = end_pos.replace(" ", "")
                end_pos = end_pos.split(",")

                fill((int(start_pos[0]),int(start_pos[1])),(int(end_pos[0]),int(end_pos[1])),input("Type : "))

            # LOAD MAP
            elif event.key == pygame.K_F10:
                load_map(input("file name : ") + ".map")


            # SAVE MAP
            elif event.key == pygame.K_F11:
                name = input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully!")


        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.Size) * Tiles.Size
            mouse_y = math.floor(mouse_pos[1] / Tiles.Size) * Tiles.Size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush]  # Keep this as a list

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
        camera_y += Tiles.Size
    elif camera_move == 2:
        camera_y -= Tiles.Size
    elif camera_move == 3:
        camera_x += Tiles.Size
    elif camera_move == 4:
        camera_x -= Tiles.Size

    # RENDER GRAPHICS

    window.fill(Color.Blue)

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()













