from abstracts import Entity


class Ground(Entity):
    def __init__(self, xpos, ypos, width, height, color):
        Entity.__init__(self, xpos, ypos, width, height, color)

    def update(self):
        pass
