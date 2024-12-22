"""
Game module for handling the game loop and events.
"""

import sys
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE
# pylint: enable=no-name-in-module

from core.input_manager import InputManager
from core.scene_manager import SceneManager

class Game:
    """
    The Game class is responsible for handling the game loop and events.

    Attributes:
        screen (pygame.Surface): The main game screen.
        clock (pygame.time.Clock): The game clock.
        fps (int): The target frames per second.
        running (bool): A flag to indicate if the game is running.
    """

    def __init__(self, screen, fps=60):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.input_manager = InputManager()  # Initialize the InputManager

    def run(self, scene_manager: SceneManager):
        """
        Runs the game loop with the specified scene.

        Args:
            scene (Scene): The scene to run in the game loop.
        """
        while self.running and scene_manager.running:  # Check both flags
            self.input_manager.update()  # Update input states
            self.handle_global_events()  # Handle global events
            scene_manager.update(self.input_manager)  # Update the current scene
            scene_manager.render()  # Render the current scene
            pygame.display.flip()
            self.clock.tick(self.fps)

        # pylint: disable=no-member
        pygame.quit()
        # pylint: enable=no-member
        sys.exit()

    def handle_global_events(self):
        """
        Handles global events such as quitting the game.
        """
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False
