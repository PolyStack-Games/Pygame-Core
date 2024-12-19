"""Dataclasses for the core module."""

from dataclasses import dataclass

@dataclass
class Cords:
    """A simple dataclass to store x and y coordinates."""
    x: int
    y: int

@dataclass
class Size:
    """A simple dataclass to store width and height."""
    width: int
    height: int
