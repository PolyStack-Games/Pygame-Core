class SceneManager:
    def __init__(self, initial_scene):
        self.current_scene = initial_scene

    def run(self, screen):
        while self.current_scene:
            self.current_scene = self.current_scene.run(screen)