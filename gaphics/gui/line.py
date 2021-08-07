import pygame

from top_ide.gaphics.gui.fixedsizesurface import Surface


class Line(Surface):

    def __init__(self, rect, parent=None):
        super(Line, self).__init__(rect, parent)
        self.design["background col"] = pygame.Color(14, 14, 14)
        self.design["hovered col"] = pygame.Color(16, 16, 16)



