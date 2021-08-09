from top_ide.gaphics.gui.content.textcontent import TextContentInternal


class BlockRenderer:

    def __init__(self):
        pass

    def can_render(self, definition:str):
        return True # todo


class BlockRendererManager:

    def __init__(self):
        self.renderers = []




class DefinitionBlockRenderer(BlockRenderer):

    def __init__(self):
        super().__init__()

    def can_render(self, definition:str):
        return True

    def render(self, definition:str):
        return TextContentInternal().render(definition)