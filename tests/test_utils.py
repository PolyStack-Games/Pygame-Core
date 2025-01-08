"""
Tests for the utils module.
"""

import pygame
from pygame_core.utils import check_collision

def test_check_collision():
    """
    Test that the check_collision function works correctly.
    """
    rect1 = pygame.Rect(0, 0, 50, 50)
    rect2 = pygame.Rect(25, 25, 50, 50)
    rect3 = pygame.Rect(100, 100, 50, 50)

    assert check_collision(rect1, rect2) is True
    assert check_collision(rect1, rect3) is False
