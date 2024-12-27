"""
This module contains the InputManager class, which is responsible for handling input from the user.
"""

from typing import Tuple
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import KEYUP, MOUSEBUTTONUP, MOUSEBUTTONDOWN
# pylint: enable=no-name-in-module

class InputManager:
    """
    Handles input from the user, including key states and mouse interactions.

    Attributes:
        keys_pressed (list): Current frame's key press states.
        keys_released (list): Keys that were released in the current frame.
        mouse_pos (tuple): The current mouse position.
        mouse_buttons (list): Current frame's mouse button states.
    """

    def __init__(self):
        self.keys_pressed: list = pygame.key.get_pressed()
        self.keys_released: list = []
        self.mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        self.mouse_clicked_down: dict = {0: False, 1: False, 2: False}
        self.mouse_clicked_up: dict = {0: False, 1: False, 2: False}
        self.mouse_button: int = 0

    def update(self):
        """
        Updates the input state. Should be called once per frame.
        """
        self.keys_pressed = pygame.key.get_pressed()
        self.keys_released = []
        self.mouse_clicked_up = {0: False, 1: False, 2: False}
        self.mouse_clicked_down = {0: False, 1: False, 2: False}

        # Capture mouse state
        self.mouse_pos = pygame.mouse.get_pos()

        # Capture key release events
        for event in pygame.event.get():
            if event.type == KEYUP:
                self.keys_released.append(event.key)
            if event.type == MOUSEBUTTONUP:
                self.mouse_clicked_up[self.mouse_button] = True
            if event.type == MOUSEBUTTONDOWN:
                self.mouse_clicked_down[self.mouse_button] = True

    def is_pressed(self, key) -> bool:
        """
        Check if a specific key is currently pressed.

        Args:
            key (int): The key to check (e.g., pygame.K_UP).

        Returns:
            bool: True if the key is pressed, False otherwise.
        """
        return self.keys_pressed[key]

    def is_released(self, key) -> bool:
        """
        Check if a specific key was released in the current frame.

        Args:
            key (int): The key to check (e.g., pygame.K_UP).

        Returns:
            bool: True if the key was released, False otherwise.
        """
        return key in self.keys_released

    def is_rect_clicked_up(self, rect: pygame.Rect, button=0) -> bool:
        """
        Check if a specific mouse button clicked within a given pygame.Rect.
        This checks on mouse Up.

        Args:
            rect (pygame.Rect): The rectangle to check for clicks.
            button (int): The mouse button to check (0=Left, 1=Middle, 2=Right).

        Returns:
            bool: True if the specified mouse button clicked within the rect, False otherwise.
        """
        self.mouse_button = button
        return (
            self.mouse_clicked_up[button]
            and rect.collidepoint(self.mouse_pos)
        )

    def is_rect_clicked_down(self, rect: pygame.Rect, button=0) -> bool:
        """
        Check if a specific mouse button clicked within a given pygame.Rect.
        This checks on mouse Down.

        Args:
            rect (pygame.Rect): The rectangle to check for clicks.
            button (int): The mouse button to check (0=Left, 1=Middle, 2=Right).

        Returns:
            bool: True if the specified mouse button clicked within the rect, False otherwise.
        """
        self.mouse_button = button
        return (
            self.mouse_clicked_down[button]
            and rect.collidepoint(self.mouse_pos)
        )
