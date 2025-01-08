"""
Tests for the Game class.
"""

import pygame

from pygame_core import create_game_context
from pygame_core.game import Game
from tests.test_scene import MockScene


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
    game_context = create_game_context()
    game_context.scene_manager.set_initial_scene(MockScene(screen, game_context))
    # Simulate quitting
    # pylint: disable=no-member
    game_context.scene_manager.update(game.input_manager)
    # pylint: enable=no-member

    assert not game_context.scene_manager.current_scene.running
