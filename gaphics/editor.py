import pygame
import gui.button as boo #todo remove
from fonts.font_manager import FontManager
from top_ide.gaphics.gui.BooleanLogicField import BooleanLogicBlock
from top_ide.gaphics.gui.fixedsizesurface import Surface, FixedPosSubsSurface
from top_ide.gaphics.gui.line import Line, LineSurface
from top_ide.gaphics.gui.lines.function_definition import FunctionDefinition

pygame.init()
screen = pygame.display.set_mode((700,400))
running = True

fontmanager = FontManager()


main_surf = FixedPosSubsSurface((698,400))

line_surf = LineSurface((600,190))

main_surf.add_sub_surface(line_surf,(5,55))

line_surf.add_line(FunctionDefinition((500,30),fontmanager))

line_surf.add_line(Line((500,30)))
line_surf.add_line(Line((500,30)))
#line_surf.add_line(Line((500,30)))
#line_surf.add_line(Line((500,30)))
#line_surf.add_line(Line((500,30)))
#line_surf.add_line(Line((500,30)))
#line_surf.add_line(Line((500,30)))
#line_surf.add_line(Line((500,30)))



#main_surf.add_sub_surface(LatexRenderer((500,30)),(4,68))


state = {"mouse pos": (0,0),
         "hovered surface": None,
         }

while running:
    updates = {"mouse moved": False,
               }
    # handle all new events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            updates["mouse moved"] = True

    # handle updates:
    if updates["mouse moved"]:

        old_surface = state["hovered surface"]

        # hover new surface
        state["mouse pos"] = pygame.mouse.get_pos()
        new_surface = main_surf.what_is_below(state["mouse pos"])
        if new_surface is not old_surface:
            state["hovered surface"] = new_surface
            if old_surface is not None: # un-hover old surface
                old_surface.mouse_moving_away_from()  # todo rename?
            if new_surface is not None: # hover new surface
                new_surface.mouse_moving_onto() # todo rename?

    screen.blit(main_surf.getImg(),(0,0))
    pygame.display.flip()


    #button = boo.Button((130,30),"hello World!", fontmanager.getFont("regular"))
    #button2 = boo.Button((130, 30), "hello World!", fontmanager.getFont("regular"))

    #boolLogicSurface = BooleanLogicBlock("(((a)∨(b))∧((¬(c))→((d)∨(b))))", fontmanager.getFont("regular"))
    #button.mouse_moving_onto()

    #latexer = LatexRenderer((300,100))

    #screen.blit(boolLogicSurface.getImg(),(30,130))
    #screen.blit(button.draw(),(400,40))
    #screen.blit(button2.draw(), (400, 70))
    #screen.blit(latexer.draw(),(0,0))