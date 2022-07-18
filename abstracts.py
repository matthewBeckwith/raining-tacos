from pygame import font, mouse, sprite, Surface, Rect
from settings import Color

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

class Button(sprite.Sprite):  
    def __init__(self, text, xpos, ypos, width, height, font_size, action=None):
        sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.blue_color = Color.SKY.value
        self.white_color = Color.PLAYER.value
        self.rect = Rect(xpos, ypos, width, height)
        
        #TODO: change from a color to an image / spritesheet
        self.btn = Surface((width, height))
        self.btn.convert()
        self.btn.set_alpha(0)
        #TODO: End
        
        self.btnfnt = font.SysFont('Arial', font_size)
        self.content = self.btnfnt.render(text, True, self.white_color)
        self.contentpos = self.content.get_rect()
        self.contentpos.centerx = self.rect.centerx
        self.contentpos.centery = self.ypos + 35

        self.action = action

    def draw(self, screen):
        screen.blit(self.btn, self.rect)
        screen.blit(self.content, self.contentpos)

    def update(self):
        lft_click = mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse.get_pos()):
            self.btn.set_alpha(128)
            if lft_click == 1 and self.action is not None:
                self.action()
        else:
            self.btn.set_alpha(0)