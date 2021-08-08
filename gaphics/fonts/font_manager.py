import os
import pygame


class FontManager:

    def __init__(self):
        self.fonts = {}

        font = pygame.font.Font(os.path.join("data", "fonts", "juliamono", 'JuliaMono-Regular.ttf'), 16)
        self.fonts["regular"] = font

        font2 = pygame.font.Font(os.path.join("data", "fonts", "stix-font","static_ttf", 'STIXTwoMath-Regular.ttf'), 20)
        self.fonts["math1"] = font2

        font3 = pygame.font.Font(os.path.join("data", "fonts", "latin modern math", 'latinmodern-math.otf'),20)
        self.fonts["math2"] = font3

    def getFonts(self):
        return self.fonts

    def getFont(self, key):
        return self.fonts[key]