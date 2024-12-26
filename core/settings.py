"""Settings for the game."""

from dataclasses import dataclass, field, asdict
import json

@dataclass
class Settings:
    """
    A class to store all settings for the game.

    Example (Create Settings Instance with few tweaks):
    context_settings = Settings.from_dict({"fps": 30, "screen_width": 1280})

    Example (Combine Multiple Configurations):
    base_config = {"screen_width": 800, "screen_height": 600, "fps": 60}
    user_config = {"fps": 120}  # User prefers a higher frame rate
    theme_config = {"colors": {"background": (50, 50, 50)}}

    # Merge configurations
    merged_config = {**base_config, **user_config, **theme_config}
    settings = Settings.from_dict(merged_config)
    """
    screen_width: int = 800
    screen_height: int = 600
    fps: int = 60
    colors: dict = field(default_factory=lambda: {
        "background": (0, 0, 0),
        "player": (255, 255, 255),
    })

    @classmethod
    def from_dict(cls, config):
        """
        Create a Settings instance from a partial dictionary.
        Unspecified fields will use default values.
        """
        default_values = asdict(cls())  # Get default values
        default_values.update(config)  # Override with provided config
        return cls(**default_values)

    def to_dict(self):
        """Convert the settings to a dictionary."""
        return asdict(self)

    def save(self, filepath):
        """Save settings to a JSON file."""
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def load(cls, filepath):
        """Load settings from a JSON file."""
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return cls.from_dict(data)
