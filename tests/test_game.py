"""
Tests for the Game class.
"""

import pygame
from core.game import Game

def test_game_initialization():
    """
    Test that the Game class initializes
    """
    screen = pygame.Surface((800, 600))
    game = Game(screen, fps=30)

    assert game.fps == 30
    assert game.running is True

def test_game_quits():
    """
    Test that the Game class quits correctly
    """
    screen = pygame.Surface((800, 600))
    game = Game(screen)

    # Simulate quitting
    # pylint: disable=no-member
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    # pylint: enable=no-member
    game.handle_events()

    assert not game.running
