"""
This module contains the Entity class, which is the base class for all entities in the game.
"""

from pygame import Color, Rect, Surface, draw, Vector2

from pygame_core.dataclasses import Size

class Entity:
    """
    The Entity class is the base
    class for all entities in the game.
    """

    def __init__(self, cords: Vector2, size: Size, color: Color):
        self.rect: Rect = Rect(cords.x, cords.y, size.width, size.height)
        self.color: Color = color

    def draw(self, screen: Surface):
        """
        Draws the entity on the screen.
        """
        draw.rect(screen, self.color, self.rect)

    def move(self, cords: Vector2):
        """
        Moves the entity by the specified amount in the x and y directions.
        """
        self.rect.x += cords.x
        self.rect.y += cords.y
