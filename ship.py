import pygame
from const import *
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('playerShip2_blue.png').convert()
        # self.image.fill(GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.8 / 2
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speedx = 0
        self.xp = 100
        self.bonus_gun = False
        self.bonus_gun_timer = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.speedx = -ROCKET_SPEED
        elif key[pygame.K_d]:
            self.speedx = ROCKET_SPEED
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        now = pygame.time.get_ticks()
        if self.bonus_gun and now - self.bonus_gun_timer > 10000:
            self.bonus_gun_timer = now
            self.bonus_gun = False
