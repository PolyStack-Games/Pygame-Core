"""Wrappers for functions that enforce certain types of arguments."""
from dataclasses import dataclass
from functools import wraps
from inspect import signature

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

def enforce_size(*arg_names):
    """
    Decorator to enforce that specific arguments are converted to Size objects.

    Parameters:
        arg_names (str): The names of the arguments to be converted.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function argument names
            sig = signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Convert specified arguments
            for arg_name in arg_names:
                if arg_name in bound_args.arguments:
                    bound_args.arguments[arg_name] = Size.from_any(bound_args.arguments[arg_name])

            return func(*bound_args.args, **bound_args.kwargs)
        return wrapper
    return decorator
