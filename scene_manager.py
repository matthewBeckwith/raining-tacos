from screens import title_screen, game_screen


class SceneManager(object):
    def __init__(self):
        self.game = None
        self.scene = None
        self.prev_scene = None
        self.stack = None
        self.go_to(title_screen.TitleScreen())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

        if isinstance(scene, title_screen.TitleScreen):
            self.stack = [scene]
            self.prev_scene = []
        if isinstance(scene, game_screen.GameScreen):
            self.game = scene
        else:
            if len(self.stack) > 0:
                previous = self.stack.pop()
            if len(self.prev_scene) > 0:
                self.prev_scene.pop()

            self.prev_scene.append(previous)
            self.stack.append(scene)
