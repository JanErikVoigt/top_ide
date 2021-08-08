from top_ide.gaphics.fonts.font_manager import FontManager
from top_ide.gaphics.gui.content.content import Content


class FunctionRenderer(Content):


    def __init__(self, fontmanager:FontManager):
        super().__init__(self, fontmanager=fontmanager)


    def render(self, definition):
        pass