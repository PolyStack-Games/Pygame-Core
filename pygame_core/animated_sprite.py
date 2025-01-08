"""
Module for handling animated sprites
"""

import pygame
from pygame import Surface, Vector2
from pygame_core.dataclasses import Size, enforce_size, SpriteSheet

class AnimatedSprite:
    """
    Class for handling animated sprites
    """

    @enforce_size("size")
    def __init__(self, sprite_sheet: SpriteSheet, size: Size, upscale=1):
        self.size: Size = size
        self.sprite_sheet: SpriteSheet = sprite_sheet
        self.upscale = upscale
        self.sprite_sheet.load_frames(self.size)

    def update(self):
        """
        Method for updating the sprite
        """
        now = pygame.time.get_ticks()
        self.sprite_sheet.animate(now)

    def draw(self, screen: Surface, vector2: Vector2):
        """
        Method for drawing the sprite
        """
        _size = (self.size.width * self.upscale, self.size.height * self.upscale)
        _sprite = self.sprite_sheet.frames[self.sprite_sheet.current_frame]
        source = pygame.transform.scale(_sprite, _size)
        screen.blit(source, vector2)
