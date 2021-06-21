import pygame
from const import *
import random


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.bottom = random.randint(-60, 0)
        self.rect.left = random.randint(0, SCREEN_WIDTH)
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(1, 2)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.right < 0) or (self.rect.left > SCREEN_WIDTH) or (self.rect.top > SCREEN_HEIGHT):
            self.rect.bottom = random.randint(-60, 0)
            self.rect.left = random.randint(0, SCREEN_WIDTH)
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(1, 5)
