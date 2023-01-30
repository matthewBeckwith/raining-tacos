from random import randint
from settings import HEIGHT
from abstracts import Entity


class Taco(Entity):
    def __init__(self, xpos, ypos, width, height, color):
        Entity.__init__(self, xpos, ypos, width, height, color)
        self.speed = randint(3, 6)

    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -randint(20, 2000)
        else:
            self.rect.y += self.speed
