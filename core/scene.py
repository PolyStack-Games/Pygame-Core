"""
This module contains the Scene class
"""

class Scene:
    """
    The Scene class is the base class for all scenes in the game.

    Attributes:
        screen (pygame.Surface): The main game screen.
        running (bool): A flag to indicate if the scene is running.

    Methods:
        update():
            Updates the scene.
        render():
            Renders the scene.
    """

    def __init__(self, screen):
        self.screen = screen
        self.running = True

    def update(self):
        """Updates the scene."""
        raise NotImplementedError

    def render(self):
        """Renders the scene."""
        raise NotImplementedError
