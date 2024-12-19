"""
Game module for handling the game loop and events.
"""

import sys
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import QUIT

from core.scene import Scene
# pylint: enable=no-name-in-module

class Game:
    """
    The Game class is responsible for handling the game loop and events.

    Attributes:
        screen (pygame.Surface): The main game screen.
        clock (pygame.time.Clock): The game clock.
        fps (int): The target frames per second.
        running (bool): A flag to indicate if the game is running.

    Methods:
        run(scene):
            Runs the game loop with the specified scene.
        handle_events():
            Handles pygame events such as quitting the game.
    """

    def __init__(self, screen, fps=60):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

    def run(self, scene: Scene):
        """
        Runs the game loop with the specified scene.

        Args:
            scene (Scene): The scene to run in the game loop.
        """
        while self.running:
            self.handle_events()
            scene.update()
            scene.render(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

        # pylint: disable=no-member
        pygame.quit()
        # pylint: enable=no-member
        sys.exit()

    def handle_events(self):
        """
        Handles pygame events such as quitting the game
        by setting the running flag to False.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
