"""
This module contains the Scene class
"""

from core.game_context import GameContext
from core.input_manager import InputManager


class Scene:
    """
    The Scene class is the base class for all scenes in the game.
    """

    def __init__(self, screen, game_context: GameContext):
        self.screen = screen
        self.game_context = game_context
        self.running = True

    def update(self, input_manager: InputManager):
        """
        Updates the scene. Override in subclasses.

        Args:
            input_manager (InputManager): The input manager to query input states.
        """
        raise NotImplementedError

    def render(self):
        """
        Renders the scene. Override in subclasses.
        """
        raise NotImplementedError
