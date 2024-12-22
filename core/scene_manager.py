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
        update(input_manager):
            Updates the current scene with input states.
        render():
            Renders the current scene.
    """
    def __init__(self, initial_scene: Scene):
        self.current_scene = initial_scene
        self.running = True

    def update(self, input_manager):
        """
        Updates the current scene with input states.

        Args:
            input_manager (InputManager): The input manager to query input states.
        """
        if self.current_scene:
            next_scene = self.current_scene.update(input_manager)
            if not self.current_scene.running:  # If the current scene stops, stop the SceneManager
                self.running = False
            elif next_scene:  # Transition to the next scene
                self.current_scene = next_scene

    def render(self):
        """
        Renders the current scene.
        """
        if self.current_scene:
            self.current_scene.render()
