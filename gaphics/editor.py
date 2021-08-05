import pygame
import gui.button as boo #todo remove
from fonts.font_manager import FontManager
from top_ide.gaphics.gui.BooleanLogicField import BooleanLogicBlock

pygame.init()
screen = pygame.display.set_mode((700,400))
running = True

fontmanager = FontManager()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(22,22,22))

    button = boo.Button((100,100),"hello World!", fontmanager.getFont("regular"))

    boolLogicSurface = BooleanLogicBlock("(((a)∨(b))∧((¬(c))→((d)∨(b))))", fontmanager.getFont("regular"))
    screen.blit(boolLogicSurface.getImg(),(30,130))

    screen.blit(button.draw(),(0,0))
    pygame.display.flip()
