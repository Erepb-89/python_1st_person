# game settings
import math

WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# sprite_settings
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# player_settings
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKY_BLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARK_BROW = (97, 61, 25)
DARK_ORANGE = (255, 140, 0)
