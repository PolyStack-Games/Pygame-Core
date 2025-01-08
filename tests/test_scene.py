"""
Tests for the Scene class and its subclasses.
"""

import pygame

from pygame_core import create_game_context
from pygame_core.scene import Scene

class MockScene(Scene):
    """
    A mock scene that does nothing.
    """
    def __init__(self, screen, game_context):
        super().__init__(screen, game_context)
        self.running = True

    def update(self, input_manager):
        """Test that the Scene class initializes."""
        self.running = False  # Stop the scene
        _ = input_manager  # Avoid unused variable warning

    def render(self):
        """Test that the Scene class initializes"""

def test_scene_manager_initialization():
    """
    Test that the SceneManager class initializes.
    """
    game_context = create_game_context()
    screen = pygame.Surface((800, 600))
    mock_scene = MockScene(screen, game_context)
    game_context.scene_manager.set_initial_scene(mock_scene)

    assert game_context.scene_manager.current_scene == mock_scene

def test_scene_manager_transition():
    """
    Test that the SceneManager class transitions between scenes.
    """
    game_context = create_game_context()
    screen = pygame.Surface((800, 600))

    class NextScene(MockScene):
        """
        A mock scene that transitions to the next scene.
        """
        def update(self, input_manager):
            """Test that the Scene class initializes."""
            return None  # Transition ends here

    mock_scene = MockScene(screen, game_context)
    next_scene = NextScene(screen, game_context)

    game_context.scene_manager.set_initial_scene(mock_scene)
    assert game_context.scene_manager.current_scene == mock_scene
    game_context.scene_manager.current_scene = next_scene
    assert game_context.scene_manager.current_scene == next_scene
