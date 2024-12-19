"""
The asset_manager module contains the AssetManager class, which is a utility class
for loading and caching game assets such as images and sounds.
"""

import pygame

class AssetManager:
    """
    AssetManager is a utility class for loading and caching game assets such as images and sounds.

    Attributes:
        _cache (dict): A dictionary to store cached assets to avoid reloading them multiple times.

    Methods:
        load_image(path):
            Loads an image from the specified path and caches it.
            If the image is already cached, returns the cached image.
        load_sound(path):
            Loads a sound from the specified path and caches it.
            If the sound is already cached, returns the cached sound.
    """
    _cache = {}

    @staticmethod
    def load_image(path):
        """
        Loads an image from the specified path and caches it.
        If the image is already cached, returns the cached image.

        Args:
            path (str): The file path to the image.

        Returns:
            pygame.Surface: The loaded image.
        """
        if path not in AssetManager._cache:
            AssetManager._cache[path] = pygame.image.load(path).convert_alpha()
        return AssetManager._cache[path]

    @staticmethod
    def load_sound(path):
        """
        Loads a sound from the specified path and caches it.
        If the sound is already cached, returns the cached sound.

        Args:
            path (str): The file path to the sound.

        Returns:
            pygame.mixer.Sound: The loaded sound.
        """
        if path not in AssetManager._cache:
            AssetManager._cache[path] = pygame.mixer.Sound(path)
        return AssetManager._cache[path]
