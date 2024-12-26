"""Dataclasses for the core module."""

from dataclasses import dataclass

@dataclass
class Cords:
    """A simple dataclass to store x and y coordinates."""
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Cords):
            return Cords(self.x + other.x, self.y + other.y)
        if isinstance(other, tuple) and len(other) == 2:
            return Cords(self.x + other[0], self.y + other[1])
        raise TypeError(f"Unsupported operand type(s) for +: 'Cords' and '{type(other).__name__}'")

    def __iadd__(self, other):
        if isinstance(other, Cords):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, tuple) and len(other) == 2:
            self.x += other[0]
            self.y += other[1]
        else:
            text = f"Unsupported operand type(s) for +=: 'Cords' and '{type(other).__name__}'"
            raise TypeError(text)
        return self

    def __sub__(self, other):
        if isinstance(other, Cords):
            return Cords(self.x - other.x, self.y - other.y)
        if isinstance(other, tuple) and len(other) == 2:
            return Cords(self.x - other[0], self.y - other[1])
        raise TypeError(f"Unsupported operand type(s) for -: 'Cords' and '{type(other).__name__}'")

    def __isub__(self, other):
        if isinstance(other, Cords):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, tuple) and len(other) == 2:
            self.x -= other[0]
            self.y -= other[1]
        else:
            text = f"Unsupported operand type(s) for -=: 'Cords' and '{type(other).__name__}'"
            raise TypeError(text)
        return self

    @classmethod
    def from_any(cls, value):
        """Converts various types into a Cords object."""
        if isinstance(value, tuple) and len(value) == 2:
            return cls(x=value[0], y=value[1])
        if isinstance(value, list) and len(value) == 2:
            return cls(x=value[0], y=value[1])
        if isinstance(value, dict) and "x" in value and "y" in value:
            return cls(x=value["x"], y=value["y"])
        if isinstance(value, cls):
            return value
        raise TypeError(f"Cannot convert {type(value)} to Cords")


@dataclass
class Size:
    """A simple dataclass to store width and height."""
    width: int
    height: int

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
