"""Dataclasses for the core module."""

from dataclasses import dataclass

from pygame import Surface, Rect

from core.wrappers import enforce_size

@dataclass
class Size:
    """A simple dataclass to store width and height."""
    width: float
    height: float

    def __add__(self, other):
        if isinstance(other, Size):
            return Size(self.width + other.width, self.height + other.height)
        if isinstance(other, tuple) and len(other) == 2:
            return Size(self.width + other[0], self.height + other[1])
        raise TypeError(f"Unsupported operand type(s) for +: 'Size' and '{type(other).__name__}'")

    def __iadd__(self, other):
        if isinstance(other, Size):
            self.width += other.width
            self.height += other.height
        elif isinstance(other, tuple) and len(other) == 2:
            self.width += other[0]
            self.height += other[1]
        else:
            text = f"Unsupported operand type(s) for +=: 'Size' and '{type(other).__name__}'"
            raise TypeError(text)
        return self

    def __sub__(self, other):
        if isinstance(other, Size):
            return Size(self.width - other.width, self.height - other.height)
        if isinstance(other, tuple) and len(other) == 2:
            return Size(self.width - other[0], self.height - other[1])
        raise TypeError(f"Unsupported operand type(s) for -: 'Size' and '{type(other).__name__}'")

    def __isub__(self, other):
        if isinstance(other, Size):
            self.width -= other.width
            self.height -= other.height
        elif isinstance(other, tuple) and len(other) == 2:
            self.width -= other[0]
            self.height -= other[1]
        else:
            text = f"Unsupported operand type(s) for -=: 'Size' and '{type(other).__name__}'"
            raise TypeError(text)
        return self

    @classmethod
    def from_any(cls, value):
        """Converts various types into a Size object."""
        if isinstance(value, tuple) and len(value) == 2:
            return cls(width=value[0], height=value[1])
        if isinstance(value, list) and len(value) == 2:
            return cls(width=value[0], height=value[1])
        if isinstance(value, dict) and "width" in value and "height" in value:
            return cls(width=value["width"], height=value["height"])
        if isinstance(value, cls):
            return value
        raise TypeError(f"Cannot convert {type(value)} to Size")

@dataclass
class SpriteSheet:
    """A class to store the sprite animation data."""
    sprite_sheet: Surface
    num_frames: int
    frame_duration: int
    current_frame: int = 0
    last_update: int = 0

    def __init__(self, sprite_sheet: Surface, num_frames: int, frame_duration: int):
        self.sprite_sheet = sprite_sheet
        self.num_frames = num_frames
        self.frame_duration = frame_duration
        self.frames = []
        _width = self.sprite_sheet.get_width() // self.num_frames
        _height = self.sprite_sheet.get_height()
        self.load_frames(Size(_width, _height))

    @enforce_size("size")
    def load_frames(self, size: Size):
        """
        Load the frames of the sprite sheet.

        Args:
            size (Size): The size of the frames.
        """
        for i in range(self.num_frames):
            rect = Rect(i * size.width, 0, size.width, size.height)
            frame = self.sprite_sheet.subsurface(rect)
            self.frames.append(frame)

    def animate(self, now: int):
        """
        Animate the sprite.

        Args:
            now (int): The current time in milliseconds.
        """
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.last_update = now
