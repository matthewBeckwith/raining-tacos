from pygame import font, sprite, KEYDOWN, K_SPACE
from random import randint
from settings import Color, WIDTH, HEIGHT, TITLE
from abstracts import Scene
from screens.game_screen import GameScreen
from components.ground import Ground
from components.taco import Taco


class TitleScreen(Scene):
    def __init__(self):
        super(TitleScreen, self).__init__()
        self.font = font.SysFont('Arial', 56)
        self.smfont = font.SysFont('Arial', 16)
        self.ground = Ground(0, (HEIGHT - 32), WIDTH, 32, Color.GROUND.value)
        self.tacos = sprite.Group()

        for _ in range(10):
            self.tacos.add(Taco(randint(2, WIDTH - 17), -randint(20, 2000), 30, 15, Color.TACO.value))

    def render(self, screen):
        screen.fill(Color.SKY.value)

        title = self.font.render(TITLE, True, Color.PLAYER.value)
        titlepos = title.get_rect()
        titlepos.centerx = screen.get_rect().centerx
        titlepos.centery = 100

        text = self.smfont.render("Press <SPACE> to Start", True, Color.PLAYER.value)
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_height() - 100

        self.tacos.draw(screen)
        screen.blit(title, titlepos)
        screen.blit(text, textpos)
        self.ground.draw(screen)

    def update(self):
        self.tacos.update()

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    self.manager.go_to(GameScreen(0))
