"""Wrappers for functions that enforce certain types of arguments."""

from functools import wraps
from inspect import signature

from core.dataclasses import Size

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
