"""
Tests for the Entity class.
"""

from core.entity import Entity

def test_entity_initialization():
    """
    Test that the Entity class initializes
    """
    entity = Entity((10, 20), (50, 60), (255, 0, 0))

    assert entity.rect.x == 10
    assert entity.rect.y == 20
    assert entity.rect.width == 50
    assert entity.rect.height == 60
    assert entity.color == (255, 0, 0)

def test_entity_movement():
    """
    Test that the Entity class moves correctly
    """
    entity = Entity((10, 20), (50, 60), (255, 0, 0))
    entity.move((5, -10))
    assert entity.rect.x == 15
    assert entity.rect.y == 10
