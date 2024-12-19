import pygame

class AssetManager:
    _cache = {}

    @staticmethod
    def load_image(path):
        if path not in AssetManager._cache:
            AssetManager._cache[path] = pygame.image.load(path).convert_alpha()
        return AssetManager._cache[path]

    @staticmethod
    def load_sound(path):
        if path not in AssetManager._cache:
            AssetManager._cache[path] = pygame.mixer.Sound(path)
        return AssetManager._cache[path]
