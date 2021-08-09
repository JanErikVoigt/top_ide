import pygame

from top_ide.gaphics.gui.content.content import ContentRenderer
from top_ide.gaphics.gui.surface import Surface, FixedPosSubsSurface


class Line(FixedPosSubsSurface):

    def __init__(self, rect, parent=None):
        super(Line, self).__init__(rect, parent)
        self.design["background col"] = pygame.Color(14, 14, 14)
        self.design["hovered col"] = pygame.Color(16, 16, 16)

        #viewmode-buttons:
        amount = 4
        rect_size = 9
        viewmodes = FixedPosSubsSurface(((rect_size+1)*amount-1,rect_size), self)
        viewmodes.design["background transparent"] = True
        for i in range(amount):
            viewmode = Surface((rect_size,rect_size),viewmodes)
            viewmode.design["background col"] = pygame.Color(80,80,80)
            viewmodes.add_sub_surface(viewmode,(i*(rect_size+1),0))

        self.add_sub_surface(viewmodes, pos=(self.get_rect()[0]- 40,1))


class LineSurface(FixedPosSubsSurface):

    def __init__(self, rect, parent=None):
        super().__init__(rect, parent)
        #self.design["background col"] = pygame.Color(14, 14, 14)
        #self.design["hovered col"] = pygame.Color(16, 16, 16)
        self.lines = []

    def add_line(self, line: Line):
        pos = None
        if len(self.sub_surfaces) > 0:
            last_y = self.get_pos_of_subsurf(-1)[1]
            new_y = last_y + self.sub_surfaces[-1].get_rect()[1] + 2
            pos = (2, new_y)
        else:
            pos = (2, 2)

        if pos is not None:
            self.add_sub_surface(line, pos)


