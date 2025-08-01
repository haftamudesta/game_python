import pygame
from random import randint
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720,
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
surf = pygame.Surface((100, 200))
surf.fill("blue")
x = 100
player_direction = pygame.math.Vector2()
player_speed = 300
clock = pygame.time.Clock()
print("pygame version:", pygame.__version__)
player_surface = pygame.image.load(
    join("images", "player.png")).convert_alpha()
player_rect = player_surface.get_rect(
    center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

meteor_surface = pygame.image.load(join("images", "meteor.png"))
meteor_rect = meteor_surface.get_rect(
    center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surface = pygame.image.load(join("images", "laser.png"))
laser_rect = laser_surface.get_rect(
    bottomleft=(20, WINDOW_HEIGHT-20))

star_surface = pygame.image.load("images/star.png")
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
                  for i in range(20)]
running = True

while running:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
    player_direction = player_direction.normalize(
    ) if player_direction else player_direction
    player_rect.center += player_direction * player_speed * dt

    display_surface.fill('purple')

    for position in star_positions:
        display_surface.blit(star_surface, position)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)

    display_surface.blit(player_surface, player_rect)

    pygame.display.update()
pygame.quit()
