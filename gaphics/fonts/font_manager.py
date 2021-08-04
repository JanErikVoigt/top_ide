import pygame



fonts = {}


def load_fonts():
    font = pygame.font.Font(os.path.join("data", "juliamono", 'juliaMono-Regular.ttf'), 24)
    fonts["regular"] = font
