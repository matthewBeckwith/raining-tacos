from settings import WIDTH
from abstracts import Entity


class Player(Entity):
    def __init__(self, xpos, ypos, width, height, color):
        Entity.__init__(self, xpos, ypos, width, height, color)
        self.xvel = 0
        self.left = self.right = False

    def update(self):
        if self.left:
            if self.rect.left < 0:
                self.rect.left = 0
            else:
                self.xvel = -10
        if self.right:
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            else:
                self.xvel = 10
        if not (self.left or self.right):
            self.xvel = 0

        self.rect.left += self.xvel
