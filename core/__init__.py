"""Core module for the game engine. Contains the main classes and utilities."""

from .animated_sprite import AnimatedSprite
from .game import Game
from .scene import Scene
from .scene_manager import SceneManager
from .input_manager import InputManager
from .entity import Entity
from .asset_manager import AssetManager
from .settings import Settings
from .game_context import create_game_context, GameContext
from . import utils

__all__ = [
    "AnimatedSprite",
    'Game',
    'Scene',
    'SceneManager',
    'InputManager',
    'Entity',
    'AssetManager',
    'Settings',
    'GameContext',
    'create_game_context',
    'utils',
]
