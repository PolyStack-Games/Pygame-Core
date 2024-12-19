class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError
