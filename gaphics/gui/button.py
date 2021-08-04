import pygame
from top_ide.gaphics.gui.fixedsizesurface import FixedSizeSurface


class Button(FixedSizeSurface):

    def __init__(self, rect, text, font):
        super().__init__(rect)
        self.text = text
        self.font = font

    def update_text(self, new_text):
        self.text = new_text
        self.rerender_required = True

    def draw(self):
        img = pygame.Surface(self.rect)
        img.fill(self.bg_col)

        #text
        text_img = self.font.render(self.text, True, pygame.Color(255,255,255))

        img.blit(text_img,(0,0))

        return img
