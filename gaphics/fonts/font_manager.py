import os
import pygame


class FontManager:

    def __init__(self):
        self.fonts = {}

        font = pygame.font.Font(os.path.join("data", "fonts", "juliamono", 'JuliaMono-Regular.ttf'), 16)
        self.fonts["regular"] = font

    def getFonts(self):
        return self.fonts

    def getFont(self, key):
        return self.fonts[key]