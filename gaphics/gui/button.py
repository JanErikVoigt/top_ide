import pygame
from top_ide.gaphics.gui.fixedsizesurface import FixedSizeSurface


class Button(FixedSizeSurface):

    def __init__(self, rect, text, font):
        super().__init__(rect)
        self.text = text
        self.font = font
        self.bg_col = pygame.Color(38, 38, 38)
        self.bg_col_hovered = pygame.Color(46, 46, 46)
        self.bg_col_pushed = pygame.Color(64, 64, 64)

        self.mouse_state = {"hovered": False, "down": False}

    def update_text(self, new_text):
        self.text = new_text
        self.rerender_required = True

    def draw(self):
        bg_col = self.bg_col
        if self.mouse_state["hovered"]:
            bg_col = self.bg_col_hovered

        img = pygame.Surface(self.rect, pygame.SRCALPHA)  # todo remove
        pygame.draw.rect(img, bg_col, pygame.Rect(0, 0, self.rect[0], self.rect[1]), 0, 4)

        #text
        text_img = self.font.render(self.text, True, pygame.Color(255,255,255))
        position = (self.rect[0] / 2 - text_img.get_size()[0]/2, self.rect[1] / 2 - text_img.get_size()[1]/2,)

        img.blit(text_img, position)

        return img

    def what_is_hovered(self, pos):
        if 0 <= pos[0] <= self.rect[0]:
            return self
        if 0 <= pos[1] <= self.rect[1]:
            return self
        return None

    def mouse_moving_onto(self):
        self.mouse_state["hovered"] = True

    def mouse_moving_away_from(self):
        self.mouse_state["hovered"] = False


