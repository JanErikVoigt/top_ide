import pygame

from top_ide.gaphics.fonts.font_manager import FontManager
from top_ide.gaphics.gui.block.blockrenderer import DefinitionBlockRenderer
from top_ide.gaphics.gui.content.textcontent import FontContent
from top_ide.gaphics.gui.line import Line
from top_ide.gaphics.gui.surface import Surface


class FunctionDefinition(Surface):

    def __init__(self, rect, parent=None):
        super().__init__(rect, parent)
        self.definition = "gello forld!"
        #self.fontmanager = fontmanager

    def draw(self):
        img = pygame.Surface(self.get_rect(), pygame.SRCALPHA)

        #font = self.fontmanager.getFont("math2")

        #todo text_img = FontContent().render("asdasd")


        text_img = DefinitionBlockRenderer().render(self.definition)

        #font.render("f♛:f",True, pygame.Color(255, 255, 255))
        img.blit(text_img,(2,2))

        # no subsurfaces are drawn...

        return img
