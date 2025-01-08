"""Dataclasses for the pygame_core module."""

from dataclasses import dataclass
from pygame import Surface, Rect

from pygame_core.dataclasses.size import Size, enforce_size

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
        if self.num_frames > 1:
            for i in range(self.num_frames):
                rect = Rect(i * size.width, 0, size.width, size.height)
                frame = self.sprite_sheet.subsurface(rect)
                self.frames.append(frame)
        else:
            self.frames.append(self.sprite_sheet)

    def animate(self, now: int):
        """
        Animate the sprite.

        Args:
            now (int): The current time in milliseconds.
        """
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.last_update = now
