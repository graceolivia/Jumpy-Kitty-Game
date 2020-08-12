import random

TITLE = "Zippy"
WIDTH = 480
HEIGHT = 600
FPS = 60
SPRITESHEET = "picropsheet.png"
FONT_NAME = 'arial'

#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -.12
GRAVITY = 0.7

#starting platforms
PLATFORM_LIST = [(0, HEIGHT - 30, WIDTH, 40),
                (WIDTH/2 - 50, HEIGHT * 3 /4, 100, 10),
                 (125, HEIGHT - 250, 100, 10),
                 (350, 200, 100, 10),
                 (175, 100, 50, 10)]


# define colors
WHITE = (223, 230, 233)
BLACK = (25, 32, 34)
RED = (214, 48, 49)
GREEN = (85, 239, 196)
BLUE = (9, 132, 227)

BGCOLOR = BLUE


def pastelMaker():
    red = random.randrange(200, 256)
    green = random.randrange(200, 256)
    blue = random.randrange(100, 256)
    return (red, green, blue)

PLATFORMCOLOR = pastelMaker()