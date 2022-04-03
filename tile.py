import pygame
from pygame import sprite
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        # self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        # self.image.fill(TILE_COLOR)
        self.image = pygame.image.load('sprites/tile.png')
        self.rect = self.image.get_rect(topleft = pos)
