"""A centralized container for shared game resources."""

from core.asset_manager import AssetManager
from core.settings import Settings

class GameContext:
    """A centralized container for shared game resources."""

    def __init__(self, settings=None):
        self.asset_manager = AssetManager()
        self.settings = settings or Settings()  # Use provided settings or default

    def load_assets(self, asset_config: dict):
        """
        Preloads assets based on a configuration dictionary.

        Args:
            asset_config (dict): A dictionary with asset types as
            keys and a list of asset definitions as values.

        Example:
            {
                "images": [
                    ("player", "assets/player.png"),
                    ("enemy", "assets/enemy.png")
                ],
                "sounds": [
                    ("explosion", "assets/explosion.wav"),
                    ("pickup", "assets/pickup.wav")
                ],
                "fonts": [
                    ("main_font", "assets/font.ttf", 24),
                    ("title_font", "assets/title_font.ttf", 36)
                ]
            }
        """
        for asset_type, assets in asset_config.items():
            for name, path in assets:
                if asset_type == "images":
                    self.asset_manager.load_image(name, path)
                elif asset_type == "sounds":
                    self.asset_manager.load_sound(name, path)
                elif asset_type == "fonts":
                    self.asset_manager.load_font(name, path[0], path[1])

    def update_settings(self, new_config):
        """
        Update settings dynamically with a dictionary.

        Args:
            new_config (dict): Partial settings to update.

        Example:
            game_context.update_settings({"fps": 30, "colors": {"background": (100, 100, 100)}})
        """
        self.settings = Settings.from_dict({**self.settings.to_dict(), **new_config})

def create_game_context(asset_config=None, custom_settings=None):
    """
    Creates and initializes a GameContext instance.

    Args:
        asset_config (dict, optional): A dictionary specifying assets to preload. Defaults to None.

    Returns:
        GameContext: The initialized GameContext instance.
    """
    context = GameContext(settings=custom_settings)
    if asset_config:
        context.load_assets(asset_config)
    return context
