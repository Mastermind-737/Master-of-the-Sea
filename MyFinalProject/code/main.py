# Imports libraries and modules
import sys, time, math
import pygame
from UltraColor import Color
from tiles import Tiles
from map_loader import Map_Loader
from player import Player
pygame.init()

# Camera Speed
CAMERA_SPEED = 300

# Camera Coordinates
CAMERA_X = 400
CAMERA_Y = 400

WORLD, TILES = Map_Loader.load_map("MyFinalProject\\maps\\world.map")

# Font for the fps counter
FPS_FONT = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

SKY_IMAGE = pygame.image.load("MyFinalProject\\Graphics\\World_Assets\\sky.png")
SKY = pygame.Surface(SKY_IMAGE.get_size(), pygame.HWSURFACE)
SKY.blit(SKY_IMAGE, (0, 0))

# Position of fps text on window screen
def show_fps():
    fps_overlay = FPS_FONT.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0,0))

# Creates window
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Master of the Sea"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)


current_second = 0
frame_count = 0
FPS = 0

# Counts the frames per second
def count_fps():
    global current_second, frame_count, FPS, deltatime

    if current_second == time.strftime("%S"):
        frame_count += 1
    else:
        FPS = frame_count
        frame_count = 0
        current_second = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS



# Creates the window
create_window()

player = Player("Felix")

player_w, player_h = player.width, player.height

isRunning = True
camera_move = 0

# Game Loop
while isRunning:
    # Listens for keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                camera_move = 4
                player.facing = "west"
        elif event.type == pygame.KEYUP:
            camera_move = 0
    # Temporary Camera with new pos
    camera_x_tmp = CAMERA_X
    camera_y_tmp = CAMERA_Y
    # Collision Box Offset
    offset_x = 0
    offset_y = 0
    # Camera movement logic
    if camera_move == 1:
        camera_y_tmp -= CAMERA_SPEED * deltatime
    elif camera_move == 2:
        camera_y_tmp += CAMERA_SPEED * deltatime
        offset_y = 1
    elif camera_move == 3:
        camera_x_tmp -= CAMERA_SPEED * deltatime
    elif camera_move == 4:
        camera_x_tmp += CAMERA_SPEED * deltatime
        offset_x = 1
    # New Player Coordinates
    player_x_new = offset_x + int((camera_x_tmp + window_width / 2 - player_w / 2) / Tiles.size)
    player_y_new = offset_y + int((camera_y_tmp + window_height / 2 - player_h / 2) / Tiles.size)
    
    # Only moves camera if no collision with blocked tile
    if not Tiles.is_blocked(TILES[player_x_new][player_y_new]):
        CAMERA_X = camera_x_tmp
        CAMERA_Y = camera_y_tmp

    # Render Sky
    window.blit(SKY, (0, 0))

    # Rendering Terrain Gridds
    window.blit(WORLD, (-CAMERA_X, -CAMERA_Y))

    #Render's Player 'Felix'
    player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))

    # Shows the fps on screen
    show_fps()
    
    # Updates the window
    pygame.display.update()

    # Counts fps
    count_fps()

# Quits Pygame
pygame.quit()
sys.exit()
