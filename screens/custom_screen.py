from pygame import font, KEYDOWN, K_ESCAPE
from settings import Color
from abstracts import Scene

class CustomScreen(Scene):
    def __init__(self, text):
        self.text = text
        super(CustomScreen, self).__init__()
        self.font = font.SysFont('Arial', 56)

    def render(self, screen):
        screen.fill(Color.SKY.value)
        text = self.font.render(self.text, True, Color.PLAYER.value)
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = 100
        screen.blit(text, textpos)

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.go_to(self.manager.prev_scene[0])