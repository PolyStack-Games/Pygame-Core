"""
The asset_manager module contains the AssetManager class, which is a utility class
for loading and caching game assets such as images and sounds.
"""

from pygame import image, mixer, font

class AssetManager:
    """Manages game assets like images, sounds, and fonts."""

    def __init__(self):
        self.assets = {}

    def load_image(self, name: str, path: str):
        """Load an image asset from a file."""
        if name not in self.assets:
            self.assets[name] = image.load(path).convert_alpha()
        return self.assets[name]

    def load_sound(self, name: str, path: str):
        """Load a sound asset from a file."""
        if name not in self.assets:
            self.assets[name] = mixer.Sound(path)
        return self.assets[name]

    def load_font(self, name: str, path: str, size: int):
        """Load a font asset from a file."""
        key = f"{name}_{size}"
        if key not in self.assets:
            self.assets[key] = font.Font(path, size)
        return self.assets[key]

    def get(self, name: str):
        """Get an asset by name."""
        return self.assets.get(name)
