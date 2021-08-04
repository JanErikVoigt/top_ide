import pygame
from .surface import Surface as custSurface


class Button(custSurface):

    def __init__(self, rect, text):
        super().__init__(rect)

        self.text = text


    def draw(self):
        img = super().draw()

        #text


        return img
