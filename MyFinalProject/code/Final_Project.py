# Imports pygame library and modules
import pygame, sys, time
from UltraColor import *
from textures import *
from globe import *
from map_engine import*
pygame.init()

cSec = 0
cFrame = 0
FPS = 0
c_speed = 1
###
terrain = Map_Engine.load_map("MyFinalProject\\maps\\awesome castle.map")

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
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")



# Creates the window
create_window()

isRunning = True

# Loop for movment camera
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0

# Camera movment logic
    if Globals.camera_move == 1:
        Globals.camera_y += c_speed
    elif Globals.camera_move == 2:
        Globals.camera_y -= c_speed
    elif Globals.camera_move == 3:
        Globals.camera_x += c_speed
    elif Globals.camera_move == 4:
        Globals.camera_x -= c_speed


    window.blit(Sky, (0, 0))

    # Rendering Terrain Grid
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    # Shows the fps on screen
    show_fps()
    
    # Updates the window
    pygame.display.update()

    # Counts fps
    count_fps()
    
pygame.quit()
sys.exit()