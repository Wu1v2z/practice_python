import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Pygame Arthur")
icon = pygame.image.load('images/game_icon.png')
pygame.display.set_icon(icon)

running = True

while running:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()