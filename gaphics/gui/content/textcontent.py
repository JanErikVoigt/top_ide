from top_ide.gaphics.fonts.font_manager import FontManager
from top_ide.gaphics.gui.content.content import Content, ContentRenderer
import PIL
import pygame
from PIL import ImageFont, ImageDraw


class TextContentInternal(ContentRenderer):
    fontmanager = None

    def __init__(self):
        super(TextContentInternal, self).__init__()
        if TextContentInternal.fontmanager is None:
            TextContentInternal.fontmanager = FontManager()

    def render(self, text: str):
        # todo fonts! todo custom params
        return TextContentInternal.fontmanager.getFont("regular").render(text, True, pygame.Color(200, 200, 200))


class FontContent(ContentRenderer):

    def __init__(self):
        super().__init__()


    def render(self, text:str):
        image = PIL.Image.new('RGBA', (600, 100)) # todo
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "Σ𝘧∫𝘦 f 𝒇｛ 𝑓𝑖𝑔:", fill=(200, 200, 200, 255),
                  font=ImageFont.truetype('data/fonts/latin modern math/latinmodern-math.otf', 20))

        mode = image.mode
        size = image.size
        data = image.tobytes()
        # data = image.convert("RGBA").tostring("raw", "RGBA")

        this_image = pygame.image.fromstring(data, size, mode)
        return this_image
