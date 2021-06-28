import random
import pygame
from const import *

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(20, SCREEN_WIDTH - 20)
        self.y = - 30
        self.images = ['pill_green.png', 'bolt_gold.png', 'shield_bronze.png']
        self.image = pygame.image.load(random.choice(self.images))
        self.rect = self.image.get_rect()

    def update(self):
        for i in range(30):
            self.rect.y += 0.7
