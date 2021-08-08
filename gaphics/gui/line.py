import pygame

from top_ide.gaphics.gui.fixedsizesurface import Surface







class Line(Surface):

    def __init__(self, rect, parent=None):
        super(Line, self).__init__(rect, parent)
        self.design["background col"] = pygame.Color(14, 14, 14)
        self.design["hovered col"] = pygame.Color(16, 16, 16)


class LineSurface(Surface):

    def __init__(self, rect, parent=None):
        super().__init__(rect, parent)
        #self.design["background col"] = pygame.Color(14, 14, 14)
        #self.design["hovered col"] = pygame.Color(16, 16, 16)

    def add_line(self, line: Line):
        pos = None
        if len(self.sub_surfaces) > 0:
            last_y = self.sub_surfaces[-1][0][1]
            new_y = last_y + self.sub_surfaces[-1][1].get_rect()[1] + 2
            pos = (2, new_y)
        else:
            pos = (2, 2)

        if pos is not None:
            self.add_sub_surface(line, pos)


