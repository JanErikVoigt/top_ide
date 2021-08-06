import pygame

from top_ide.gaphics.gui.fixedsizesurface import Surface


class BackgroundSurface(Surface):


    def __init__(self, rect):
        super(BackgroundSurface, self).__init__(rect)


    def draw(self):
        img = pygame.Surface(self.rect)
        img.fill(pygame.Color(22,22,22))
        return img