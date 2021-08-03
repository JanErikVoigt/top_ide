import pygame
import gui.button as boo


pygame.init()
screen = pygame.display.set_mode((700,400))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    button = boo.Button((100,100))
    screen.blit(button.draw(),(0,0))
    pygame.display.flip()
