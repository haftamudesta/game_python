import pygame
from random import randint
from os.path import join


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        # recent_keys = pygame.key.get_just_pressed()
        # if recent_keys[pygame.K_SPACE]:
        #     print("space pressed")


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720,
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
surf = pygame.Surface((100, 200))
surf.fill("blue")
x = 100
star_surf = pygame.image.load(join("images", "star.png"))
all_sprites = pygame.sprite.Group()

for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)
clock = pygame.time.Clock()
meteor_surface = pygame.image.load(join("images", "meteor.png"))
meteor_rect = meteor_surface.get_rect(
    center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surface = pygame.image.load(join("images", "laser.png"))
laser_rect = laser_surface.get_rect(
    bottomleft=(20, WINDOW_HEIGHT-20))
running = True

while running:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update(dt)
    display_surface.fill('purple')

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)
    all_sprites.draw(display_surface)
    pygame.display.update()
pygame.quit()
