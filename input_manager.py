import pygame

class InputManager:
    def __init__(self):
        self.keys = {}

    def update(self):
        self.keys = pygame.key.get_pressed()

    def is_pressed(self, key):
        return self.keys[key]
