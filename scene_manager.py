from screens.title_screen import TitleScreen

class SceneMananger(object):
    def __init__(self):
        self.go_to(TitleScreen())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

        if isinstance(scene, TitleScreen):
            self.stack = [scene]
            self.prev_scene = []
        else:
            if len(self.stack) > 0:
                previous = self.stack.pop()
            if len(self.prev_scene) > 0:
                self.prev_scene.pop()
            
            self.prev_scene.append(previous)
            self.stack.append(scene)