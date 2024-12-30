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

    def __post_init__(self):
        """Safely initialize custom attributes."""
        object.__setattr__(self, "_custom_attributes", {})

    def __getattr__(self, name: str):
        """Dynamically access custom attributes."""
        if "_custom_attributes" in self.__dict__ and name in self._custom_attributes:
            return self._custom_attributes[name]
        raise AttributeError(f"'Settings' object has no attribute '{name}'")

    def __setattr__(self, name: str, value):
        """Safely set custom attributes."""
        if "_custom_attributes" in self.__dict__ and name not in asdict(self):
            self._custom_attributes[name] = value
        else:
            super().__setattr__(name, value)

    @classmethod
    def from_dict(cls, config:dict):
        """
        Create a Settings instance from a dictionary.
        Includes support for custom settings.
        """
        known_fields = {field.name for field in cls.__dataclass_fields__.values()}
        core_config = {k: v for k, v in config.items() if k in known_fields}
        custom_config = {k: v for k, v in config.items() if k not in known_fields}

        instance = cls(**core_config)

        # Add custom settings
        for key, value in custom_config.items():
            setattr(instance, key, value)

        return instance

    def to_dict(self):
        """Convert settings to a dictionary, including custom attributes."""
        data = asdict(self)
        data.update(self._custom_attributes)
        return data

    def save(self, filepath: str):
        """Save settings to a JSON file."""
        with open(filepath, "w", encoding='utf-8') as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def load(cls, filepath: str):
        """Load settings from a JSON file."""
        with open(filepath, "r", encoding='utf-8') as file:
            data = json.load(file)
        return cls.from_dict(data)
