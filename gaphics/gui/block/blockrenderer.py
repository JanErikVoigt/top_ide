from top_ide.gaphics.gui.content.textcontent import TextContentInternal


class BlockRenderer:

    def __init__(self):
        pass

    def can_render(self, definition:str):
        return True # todo


class BlockRendererManager:

    __instance = None

    @staticmethod
    def get_instance():
        if BlockRendererManager.__instance is None:
            BlockRendererManager.__instance = BlockRendererManager()
        return BlockRendererManager.__instance

    def __init__(self):
        if BlockRendererManager.__instance is not None:
            raise Exception("This class is a singleton!")
        self.renderers = []




class DefinitionBlockRenderer(BlockRenderer):

    def __init__(self):
        super().__init__()

    def can_render(self, definition:str):
        return True

    def render(self, definition:str):
        return TextContentInternal().render(definition)