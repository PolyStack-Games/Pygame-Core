"""
This file contains fixtures that are automatically used by all tests in the module.
"""

import pytest
import pygame

@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    """
    Automatically initialize and quit Pygame for all tests in the module.
    """
    # pylint: disable=no-member
    pygame.init()
    yield
    pygame.quit()
    # pylint: enable=no-member
