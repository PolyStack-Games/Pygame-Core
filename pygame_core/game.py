"""
Game module for handling the game loop and events.
"""

import sys

import pygame
# pylint: disable=no-name-in-module
from pygame import time, display
from pygame.constants import K_ESCAPE
# pylint: enable=no-name-in-module
# pylint: disable=cyclic-import
from pygame_core.input_manager import InputManager
from pygame_core.scene_manager import SceneManager

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
        self.clock = time.Clock()
        self.fps = fps
        self.running = True
        self.input_manager = InputManager()  # Initialize the InputManager

    def run(self, scene_manager: SceneManager):
        """
        Runs the game loop with the specified scene.

        Args:
            scene_manager (SceneManager): The scene manager to handle the game scenes.
        """
        while self.running and scene_manager.running:  # Check both flags
            self.handle_global_events()  # Handle global events
            self.input_manager.update()  # Update input states
            scene_manager.update(self.input_manager)  # Update the current scene
            scene_manager.render()  # Render the current scene
            display.flip()
            self.clock.tick(self.fps)

        # pylint: disable=no-member
        pygame.quit()
        # pylint: enable=no-member
        sys.exit()

    def handle_global_events(self):
        """
        Handles global events such as quitting the game.
        """
        if self.input_manager.is_pressed(K_ESCAPE):
            self.running = False
        # for e in event.get():
        #     if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
        #         self.running = False
# pylint: enable=cyclic-import
