import pygame
import ast
from top_ide.gaphics.gui.fixedsizesurface import FreeSizeSurface
import re

# todo rename to BooleanLogicBlock


class BooleanLogicBlock(FreeSizeSurface):

    def __init__(self, definition, font):
        super().__init__()
        self.definition = definition
        self.font = font
        self.bg_col = pygame.Color(38,38,38)
        self.definition = definition

    def draw(self):

        # render text
        text_img = self.font.render(self.definition, True, pygame.Color(200, 200, 200))

        # create background-box
        box_rect = (text_img.get_size()[0]+4,text_img.get_size()[1]+5)
        img = pygame.Surface(box_rect, pygame.SRCALPHA)  # todo remove
        pygame.draw.rect(img, self.bg_col, pygame.Rect(0, 0, box_rect[0], box_rect[1]), 0, 7)

        # draw text on box
        img.blit(text_img, (2, 2))

        # return result
        return img

    def draw_formula(self, formula):
        # match a,b,c
        pattern_var = r'\((\w)\)'
        pattern_and = r'\(...  \)'

        match_var = re.match(pattern_var, formula)
        if match_var.span()[0] == 0 and match_var.span()[1] == len(formula)+1:
            print("match var!")





