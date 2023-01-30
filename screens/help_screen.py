from pygame import font, KEYDOWN, K_ESCAPE
from settings import Color
from abstracts import Scene


class HelpScreen(Scene):
    def __init__(self):
        super(HelpScreen, self).__init__()
        self.font1 = font.SysFont('Arial', 56)
        self.font2 = font.SysFont('Arial', 24)

    def render(self, screen):
        screen.fill(Color.SKY.value)
        title = self.font1.render("Help", True, Color.PLAYER.value)
        titlepos = title.get_rect()
        titlepos.centerx = screen.get_rect().centerx
        titlepos.centery = 100
        content1 = self.font2.render("Collect Tacos to build gas,", True, Color.PLAYER.value)
        content1pos = content1.get_rect()
        content1pos.centerx = screen.get_rect().centerx
        content1pos.centery = 250
        content2 = self.font2.render("fill balloons,", True, Color.PLAYER.value)
        content2pos = content2.get_rect()
        content2pos.centerx = screen.get_rect().centerx
        content2pos.centery = 280
        content3 = self.font2.render("block the incomming threat!", True, Color.PLAYER.value)
        content3pos = content3.get_rect()
        content3pos.centerx = screen.get_rect().centerx
        content3pos.centery = 310
        screen.blit(title, titlepos)
        screen.blit(content1, content1pos)
        screen.blit(content2, content2pos)
        screen.blit(content3, content3pos)

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.go_to(self.manager.prev_scene[0])
