import pygame


class Surface:

    def __init__(self, rect, parent=None):
        self.parent = parent
        self.sub_surfaces = []
        self.rerender_required = True
        self.img = None
        self.rect = rect
        self.state = {"hovered": False}
        self.design = {"background col": pygame.Color(22, 22, 22),  # todo put at one pos?
                       "hovered col": pygame.Color(24, 24, 24),
                       "clicked col": pygame.Color(42, 42, 42),
                       "background transparent": False,
                       }

    def set_parent(self, parent):
        self.parent = parent
        self.state_changed()

    def get_rect(self):
        return self.rect

    def get_pos_of_subsurf(self, i:int):
        return (0, 0)  # override!

    def state_changed(self):
        self.rerender_required = True
        if self.parent is not None:
            self.parent.state_changed()

    def set_rect(self, new_rect):
        self.rect = new_rect
        self.state_changed()

    def sub_inside_surface(self, i: int):
        #pos = self.get_pos_of_subsurf(sub)
        #rec = sub.get_rect()
        pos = self.get_pos_of_subsurf(i)
        rec = self.sub_surfaces[i].get_rect()

        if pos[0] > self.rect[0] or pos[1] > self.rect[1]:
            return False
        if pos[0] + rec[0] < 0 or pos[1] + rec[1] < 0:
            return False
        return True

    def draw(self):
        img = pygame.Surface(self.get_rect())
        if not self.design["background transparent"]:
            if self.state["hovered"]:
                img.fill(self.design["hovered col"])
            else:
                img.fill(self.design["background col"])

        for i, surf in enumerate(self.sub_surfaces):
            if self.sub_inside_surface(i):
                pos = self.get_pos_of_subsurf(i)
                img.blit(surf.getImg(), pos)

        return img

    def add_sub_surface(self, sub_surface):
        sub_surface.set_parent(self)
        self.sub_surfaces.append(sub_surface)
        self.state_changed()

    def getImg(self):
        if self.rerender_required:
            self.img = self.draw()
            self.rerender_required = False
        return self.img

    def what_is_below(self, position):
        if 0 <= position[0] <= self.get_rect()[0] and 0 <= position[1] <= self.get_rect()[1]:
            for i,sub in enumerate(self.sub_surfaces):
                if self.sub_inside_surface(i):
                    pos = self.get_pos_of_subsurf(i)
                    hovered = sub.what_is_below((position[0] - pos[0], position[1] - pos[1]))
                    if hovered is not None:
                        return hovered
            return self
        return None

    def mouse_moving_onto(self):
        self.state["hovered"] = True
        self.state_changed()

    def mouse_moving_away_from(self):
        self.state["hovered"] = False
        self.state_changed()


class FixedPosSubsSurface(Surface):

    def __init__(self, rect, parent=None):
        super().__init__(rect=rect, parent=parent)
        self.positions = []

    def get_pos_of_subsurf(self, i):
        return self.positions[i]

    def add_sub_surface(self, sub_surface, pos):
        sub_surface.set_parent(self)
        self.sub_surfaces.append(sub_surface)
        self.state_changed()  # todo call super?
        self.positions.append(pos)



class FreeSizeSurface:

    def __init__(self):
        self.bg_col = pygame.Color(200, 200, 200)
        self.rerender_required = True
        self.img = None

    def draw(self):
        img = pygame.Surface((123, 123))  # todo remove
        img.fill(self.bg_col)
        return img

    def getImg(self):
        if self.rerender_required:
            self.img = self.draw()
            self.rerender_required = False
        return self.img


class FixedSizeSurface:

    def __init__(self, rect):
        self.rect = rect
        self.bg_col = pygame.Color(200, 200, 200)
        self.rerender_required = True
        self.img = None

    def draw(self):
        img = pygame.Surface(self.rect)
        img.fill(self.bg_col)
        return img

    def getImg(self):
        if self.rerender_required:
            self.img = self.draw()
            self.rerender_required = False
        return self.img
