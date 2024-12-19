"""
This module contains utility functions that are used in the game.
"""

from core.dataclasses import Size


def check_collision(rect1, rect2):
    """
    Check if two rectangles are colliding.

    Args:
        rect1 (pygame.Rect): The first rectangle.
        rect2 (pygame.Rect): The second rectangle.

    Returns:
        bool: True if the rectangles are colliding, False otherwise.
    """
    return rect1.colliderect(rect2)

def wrap_around_screen(rect, size: Size):
    """
    Wrap an entity around the screen if it goes off the edge.

    Args:
        rect (pygame.Rect): The entity to wrap around the screen.
        screen_width (int): The width of the screen.
        screen_height (int): The height of the screen.
    """
    if rect.left > size.width:
        rect.right = 0
    elif rect.right < 0:
        rect.left = size.width
    if rect.top > size.height:
        rect.bottom = 0
    elif rect.bottom < 0:
        rect.top = size.height
