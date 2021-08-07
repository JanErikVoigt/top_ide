import pygame
from IPython.display import display, Math, Latex
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pylatex


from top_ide.gaphics.gui.line import Line


class LatexRenderer(Line):

    def __init__(self, rect):
        super().__init__(rect)


    def draw(self):
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.gca()

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.gca()

        ax.text(0.0, 0.0, "Test", fontsize=45)
        ax.axis('off')

        canvas.draw()  # draw the canvas, cache the renderer

        image = np.fromstring(canvas.tostring_rgb(), dtype='uint8')

        img = pygame.Surface((300, 300))

        surf = pygame.surfarray.make_surface(image)

        img.blit(surf)


        return img
