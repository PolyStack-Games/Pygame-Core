"""
This module contains the SceneManager class.
"""

from pygame_core.input_manager import InputManager
from pygame_core.scene import Scene

class SceneManager:
    """
    Manages the scenes in the game and handles transitions.

    Attributes:
        current_scene (Scene): The active scene.
        running (bool): Flag to indicate if the game is running.
    """

    def __init__(self):
        self.current_scene: Scene | None = None
        self.running = True
        self.cache = {}

    def set_initial_scene(self, scene: Scene):
        """Set the initial scene for the game."""
        self.current_scene = scene

    def update(self, input_manager: InputManager):
        """
        Updates the current scene and checks for transitions.

        Args:
            input_manager (InputManager): The input manager to query input states.
        """
        if self.current_scene:
            self.current_scene.update(input_manager)
            if not self.current_scene.running:  # Check if the current scene should stop
                self.running = False

    def render(self):
        """Renders the current scene."""
        if self.current_scene:
            self.current_scene.render()

    def transition_to(self, new_scene: Scene):
        """Transition to a new scene."""
        self.current_scene = new_scene

    def cache_scene(self, scene_name: str, scene: Scene):
        """Cache a scene for later use."""
        self.cache[scene_name] = scene

    def get_cached_scene(self, scene_name: str) -> Scene:
        """Get a cached scene."""
        return self.cache.get(scene_name)

    def is_scene_cached(self, scene_name: str) -> bool:
        """Check if a scene is cached."""
        return scene_name in self.cache
