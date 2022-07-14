from pygame import sprite, Surface, Rect

class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class Entity(sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, color):
        sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        
        #TODO: change from a color to an image / spritesheet
        self.image = Surface((width, height))
        self.image.fill(color)
        self.image.convert()
        #TODO: End

        self.rect = Rect(xpos, ypos, width, height)
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update():
        raise NotImplementedError

