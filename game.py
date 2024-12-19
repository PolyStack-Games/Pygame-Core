import pygame

class Game:
    def __init__(self, screen, fps=60):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

    def run(self, scene):
        while self.running:
            self.handle_events()
            scene.update()
            scene.render(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False