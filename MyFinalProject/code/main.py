# Imports pygame library and modules
import sys, time, math
import pygame
from UltraColor import *
from textures import *
from globals import Globals
from map_engine import*
from player import * 
pygame.init()

cSec = 0
cFrame = 0
FPS = 0
c_speed = .75

terrain = Map_Engine.load_map("MyFinalProject\\maps\\world.map")

# Font for the fps counter
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("MyFinalProject\\Graphics\\World_Assets\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

# Position of fps text on window screen
def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0,0))

# Creates window and title of window
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Master of the Sea"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

# Counts the frames per second
def count_fps():
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS



# Creates the window
create_window()

player = Player("Felix")

player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.size



isRunning = True

# Loop for movment camera
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "west"
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0

# Camera movment logic
    if Globals.camera_move == 1:
        if not Tiles.Blocked_At ((round, (player_x), math.floor(player_y))):
            Globals.camera_y += 300 * deltatime
    elif Globals.camera_move == 2:
        if not Tiles.Blocked_At ((round, (player_x), math.ceil(player_y))):
            Globals.camera_y -= 300 *deltatime
    elif Globals.camera_move == 3:
        if not Tiles.Blocked_At ((math.floor, (player_x), round(player_y))):
            Globals.camera_x += 300 * deltatime
    elif Globals.camera_move == 4:
        if not Tiles.Blocked_At ((math.ceil, (player_x), round(player_y))):
            Globals.camera_x -= 300 * deltatime

    player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.size
    player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.size
    
    # Render Sky
    window.blit(Sky, (0, 0))

    # Rendering Terrain Grid
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    #Render's Player 'Felix'
    player.render(window, (window_width / 2 - player_w / 4, window_height / 2 - player_h / 4))


    # Shows the fps on screen
    show_fps()
    
    # Updates the window
    pygame.display.update()

    # Counts fps
    count_fps()
    
pygame.quit()
sys.exit()