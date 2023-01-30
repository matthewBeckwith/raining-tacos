from enum import Enum

TITLE = "It's Raining Tacos"

HEIGHT = 640
WIDTH = 480
DISPLAY = (WIDTH, HEIGHT)
FPS = 60
FLAGS = 0
DEPTH = 0


class Color(Enum):
    SKY = (66, 135, 245)
    GROUND = (89, 60, 29)
    TACO = (214, 194, 94)
    CHILI = (79, 16, 0)
    GAS = (87, 179, 18)
    PLAYER = (167, 188, 204)
