import pygame
from random import randint

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720,
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
surf = pygame.Surface((100, 200))
surf.fill("blue")
x = 100
player_surface = pygame.image.load("images/player.png")
star_surface = pygame.image.load("images/star.png")
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
                  for i in range(20)]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('purple')
    x += 0.1
    display_surface.blit(player_surface, (x, 150))
    for position in star_positions:
        display_surface.blit(star_surface, position)
    pygame.display.update()
pygame.quit()
