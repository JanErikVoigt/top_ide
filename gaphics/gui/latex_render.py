import pygame
import matplotlib.pyplot as plt

from top_ide.gaphics.gui.fixedsizesurface import FixedSizeSurface
import sympy



class LatexRenderer(FixedSizeSurface):

    def __init__(self, rect):
        super().__init__(rect)


    def draw(self):
        sympy.preview(r'$$\int_0^1 e^x\,dx$$', viewer='file', filename='test.png')

        return None
