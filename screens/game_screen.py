from pygame import font, key, sprite, KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT
from random import randint
from settings import Color, WIDTH, HEIGHT
from abstracts import Scene
from screens.pause_screen import PauseScreen
from components.player import Player
from components.ground import Ground
from components.taco import Taco

class GameScreen(Scene):
    def __init__(self, levelno):
        super(GameScreen, self).__init__()
        self.levelno = levelno
        self.difficulty = 5

        self.p = Player(((WIDTH / 2) - (32 / 2)), (HEIGHT - 96), 32, 64, Color.PLAYER.value)

        self.font = font.SysFont('Arial', 32)

        self.entities = sprite.Group()
        self.player = sprite.GroupSingle(self.p)
        self.ground = Ground(0, (HEIGHT - 32), WIDTH, 32, Color.GROUND.value)
        self.tacos = sprite.Group()

        for _ in range((10 + (self.levelno * self.difficulty))):
            self.tacos.add(Taco(randint(2, WIDTH - 17), -randint(20, 2000), 30, 15, Color.TACO.value))

        self.entities.add(self.tacos, self.player, self.ground)

    def render(self, screen):
        screen.fill(Color.SKY.value)
        level_text = self.font.render(f"LEVEL: {self.levelno}", True, Color.PLAYER.value)
        level_text_pos = level_text.get_rect()
        level_text_pos.x = 10
        level_text_pos.y = 10

        self.entities.draw(screen)
        screen.blit(level_text, level_text_pos)
    
    def update(self):
        pressed = key.get_pressed()
        self.p.left, self.p.right = [pressed[k] for k in (K_LEFT, K_RIGHT)]

        collision = sprite.groupcollide(self.player, self.tacos, False, True)

        if len(self.tacos) == 0:
            self.exit()

        self.entities.update()

    def exit(self):
        self.manager.go_to(GameScreen(self.levelno+1))

    def die(self):
        self.manager.go_to(CustomScreen("You lose!"))

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.go_to(PauseScreen())
