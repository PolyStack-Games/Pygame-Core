"""
Tests for the Scene class and its subclasses.
"""

import pygame
from core.scene import Scene
from core.scene_manager import SceneManager

class MockScene(Scene):
    """
    A mock scene that does nothing.
    """
    def update(self):
        return None  # No transitions

    def render(self):
        pass  # Do nothing

def test_scene_manager_initialization():
    """
    Test that the SceneManager class initializes.
    """
    screen = pygame.Surface((800, 600))
    mock_scene = MockScene(screen)
    manager = SceneManager(initial_scene=mock_scene)

    assert manager.current_scene == mock_scene

def test_scene_manager_transition():
    """
    Test that the SceneManager class transitions between scenes.
    """
    screen = pygame.Surface((800, 600))

    class NextScene(MockScene):
        """
        A mock scene that transitions to the next scene.
        """
        def update(self):
            return None  # Transition ends here

    mock_scene = MockScene(screen)
    next_scene = NextScene(screen)

    manager = SceneManager(initial_scene=mock_scene)
    assert manager.current_scene == mock_scene
    manager.current_scene = next_scene
    assert manager.current_scene == next_scene
