from const import *
import random
import pygame

class Bonus(pygame.sprite.Sprite):
    def __init__(self, bonus_image_dict, meteor_center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['hp', 'gun', 'shield', 'star'])
        self.image = bonus_image_dict[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = meteor_center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
