"""
This module contains the InputManager class, which is responsible for handling input from the user.
"""

import pygame

class InputManager:
    """
    The InputManager class is responsible for handling input from the user.

    Attributes:
        keys (dict): A dictionary to store the state of all keys.
    """

    def __init__(self):
        self.keys = {}

    def update(self):
        """Updates the state of all keys."""
        self.keys = pygame.key.get_pressed()

    def is_pressed(self, key):
        """
        Returns True if the specified key is pressed, False otherwise.

        Args:
            key (int): The key to check.

        Returns:
            bool: True if the key is pressed, False otherwise.
        """
        return self.keys[key]
