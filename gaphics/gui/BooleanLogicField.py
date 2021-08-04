import pygame
import ast
from top_ide.gaphics.gui.fixedsizesurface import FreeSizeSurface
import re

# todo rename to BooleanLogicBlock


class BooleanLogicBlock(FreeSizeSurface):

    def __init__(self, definition):
        super().__init__()

        self.definition = definition

    def draw(self):
        img = pygame.Surface((123, 123),pygame.SRCALPHA)  # todo remove
        pygame.draw.rect(img, self.bg_col, pygame.Rect(30, 30, 60, 60), 0, 3)

        return img

    def draw_formula(self, formula):
        # match a,b,c
        pattern_var = r'\((\w)\)'
        pattern_and = r'\(...  \)'

        match_var = re.match(pattern_var, formula)
        if match_var.span()[0] == 0 and match_var.span()[1] == len(formula)+1:
            print("match var!")





