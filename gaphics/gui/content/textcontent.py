from top_ide.gaphics.gui.content.content import Content
import PIL
import pygame
from PIL import ImageFont, ImageDraw



class FontContent(Content):

    def __init__(self):
        super().__init__()


    def render(self, text:str):
        image = PIL.Image.new('RGBA', (100, 100))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "𝘧𝘦 f 𝒇 𝑓𝑖𝑔:", fill=(200, 200, 200, 255),
                  font=ImageFont.truetype('data/fonts/latin modern math/latinmodern-math.otf', 20))

        mode = image.mode
        size = image.size
        data = image.tobytes()
        # data = image.convert("RGBA").tostring("raw", "RGBA")

        this_image = pygame.image.fromstring(data, size, mode)
        return this_image
