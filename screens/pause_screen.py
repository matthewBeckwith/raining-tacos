from pygame import font, mouse, Surface, quit, KEYDOWN, K_ESCAPE
from settings import Color, WIDTH
from abstracts import Scene, Button
from screens.help_screen import HelpScreen

class PauseScreen(Scene):
    def __init__(self):
        super(PauseScreen, self).__init__()
        self.font1 = font.SysFont('Arial', 56)
        self.font2 = font.SysFont('Arial', 24)
        self.helpbtn = Button("Help", ((WIDTH / 2) - 75), 200, 150, 75, 32, self.help_btn)

    def render(self, screen):
        screen.fill(Color.SKY.value)
        title = self.font1.render("Pause", True, Color.PLAYER.value)
        titlepos = title.get_rect()
        titlepos.centerx = screen.get_rect().centerx
        titlepos.centery = 100

        screen.blit(title, titlepos)
        self.helpbtn.draw(screen)

    def update(self):
        self.helpbtn.update()

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.go_to(self.manager.game)

    def help_btn(self):
        self.manager.go_to(HelpScreen())