import pygame
from const import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship_x, ship_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullets.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship_x
        self.rect.bottom = ship_y
        self.speed_y = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed_y
        if self.rect.top < 0:
            self.kill()
