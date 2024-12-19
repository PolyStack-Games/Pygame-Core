"""
This module contains the SceneManager class.
"""

from core.scene import Scene


class SceneManager:
    """
    The SceneManager class is responsible for managing the scenes in the game.

    Attributes:
        current_scene (Scene): The current scene that is being run.

    Methods:
        __init__(initial_scene):
            Initializes the SceneManager with the specified initial scene.
        run(screen):
            Runs the game loop with the current scene.
    """
    def __init__(self, initial_scene: Scene):
        self.current_scene = initial_scene

    def run(self, screen):
        """
        Runs the game loop with the current scene.

        Args:
            screen (pygame.Surface): The main game screen.
        """
        while self.current_scene:
            self.current_scene = self.current_scene.run(screen)
