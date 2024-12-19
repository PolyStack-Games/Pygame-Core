"""
This module contains the Entity class, which is the base class for all entities in the game.
"""

import pygame

from core.dataclasses import Cords, Size

class Entity:
    """
    The Entity class is the base
    class for all entities in the game.

    Attributes:
        rect (pygame.Rect): The rectangular area that the entity occupies.
        color (tuple): The color of the entity.

    Methods:
        draw(screen):
            Draws the entity on the screen.
        move(dx, dy):
            Moves the entity by the specified amount in the x and y directions.
    """

    def __init__(self, cords: Cords, size: Size, color: pygame.Color):
        # Convert tuples to Cords and Size if needed
        if isinstance(cords, tuple):
            cords = Cords(*cords)
        if isinstance(size, tuple):
            size = Size(*size)

        self.rect: pygame.Rect = pygame.Rect(cords.x, cords.y, size.width, size.height)
        self.color: pygame.Color = color

    def draw(self, screen):
        """
        Draws the entity on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the entity on.
        """
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, cords: Cords):
        """
        Moves the entity by the specified amount in the x and y directions.

        Args:
            dx (int): The amount to move the entity in the x direction.
            dy (int): The amount to move the entity in the y direction.
        """
        if isinstance(cords, tuple):
            cords = Cords(*cords)
        self.rect.x += cords.x
        self.rect.y += cords.y
