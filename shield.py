import pygame
from const import *

class Shield(pygame.sprite.Sprite):
    def __init__(self, ship_center):
        super().__init__()
        self.image = pygame.image.load('shield1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ship_center
        self.last_update = pygame.time.get_ticks()
        self.hide = True

    def update(self, ship_center):
        if self.hide:
            self.rect.center = -100, -100
        else:
            self.rect.center = ship_center
        now = pygame.time.get_ticks()
        if now - self.last_update > 10000:
            self.last_update = now
            self.hide = True
            # self.rect.center = (-100, -100)
