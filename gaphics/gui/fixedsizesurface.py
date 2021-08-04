import pygame


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

    subsurfaces = []

    def __init__(self, rect):
        self.rect = rect
        self.bg_col = pygame.Color(200,200,200)
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