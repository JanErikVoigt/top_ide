import pygame
from .surface import Surface as custSurface


class Button(custSurface):

    def __init__(self, rect):
        self.rect = rect
        self.bg_col = pygame.Color(200,200,200)

    def draw(self):
        img = pygame.Surface(self.rect)
        img.fill(self.bg_col)
        return img
