"""A centralized container for shared game resources."""

from pygame_core.asset_manager import AssetManager
from pygame_core.settings import Settings

class GameContext:
    """A centralized container for shared game resources."""

    def __init__(self, settings:Settings=None):
        self.asset_manager = AssetManager()
        self.settings = settings or Settings()  # Use provided settings or default
        self.scene_manager = None

    def load_assets(self, asset_config: dict):
        """
        Preloads assets based on a configuration dictionary.

        Args:
            asset_config (dict): A dictionary with asset types as
            keys and a list of asset definitions as values.

        Example:
            assets = {
                "images": [
                    {"name": "player", "path": "assets/images/player.png"},
                    {"name": "enemy", "path": "assets/images/enemy.png"}
                ],
                "sounds": [
                    {"name": "jump", "path": "assets/sounds/jump.wav"},
                    {"name": "explosion", "path": "assets/sounds/explosion.wav"}
                ],
                "fonts": [
                    {"name": "default", "path": "assets/fonts/arial.ttf", "size": 24}
                ]
            }
        """
        for asset_type, assets in asset_config.items():
            for asset in assets:
                if asset_type == "images":
                    self.asset_manager.load_image(**asset)  # Unpack {"name": ..., "path": ...}
                elif asset_type == "sounds":
                    self.asset_manager.load_sound(**asset)  # Unpack {"name": ..., "path": ...}
                elif asset_type == "fonts":
                    self.asset_manager.load_font(asset["name"], asset["path"], asset["size"])

    def update_settings(self, new_config:dict):
        """
        Update settings dynamically with a dictionary.

        Args:
            new_config (dict): Partial settings to update.

        Example:
            game_context.update_settings({"fps": 30, "colors": {"background": (100, 100, 100)}})
        """
        self.settings = Settings.from_dict({**self.settings.to_dict(), **new_config})

def create_game_context(
        asset_config:dict=None,
        custom_settings:Settings=None,
    ) -> GameContext:
    """
    Creates and initializes a GameContext instance.

    Args:
        asset_config (dict, optional): A dictionary specifying assets to preload. Defaults to None.
        custom_settings (Settings, optional): Custom game settings. Defaults to None.

    Returns:
        GameContext: The initialized GameContext instance.
    """
    context = GameContext(settings=custom_settings)
    # pylint: disable=import-outside-toplevel
    from pygame_core.scene_manager import SceneManager
    # pylint: enable=import-outside-toplevel
    context.scene_manager = SceneManager()
    if asset_config:
        context.load_assets(asset_config)
    return context
