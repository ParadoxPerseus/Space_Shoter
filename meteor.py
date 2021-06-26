import pygame
from const import *
import random


class Meteor(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30, 30))
        # self.image.fill(BROWN)

        self.image_orig = random.choice(images)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.8 / 2
        self.image_orig.set_colorkey(BLACK)
        self.rect.bottom = random.randint(-60, 0)
        self.rect.left = random.randint(0, SCREEN_WIDTH)
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(1, 1)
        self.rotate_speed = random.randint(-8, 8)
        self.angle = 0
        self.rotate_timer = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        now = pygame.time.get_ticks()
        # self.image = pygame.transform.rotate(self.image, self.rotate_speed)
        if now - self.rotate_timer > 50:
            self.rotate_timer = now
            self.angle = (self.angle + self.rotate_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.angle)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

        if (self.rect.right < 0) or (self.rect.left > SCREEN_WIDTH) or (self.rect.top > SCREEN_HEIGHT):
            self.rect.bottom = random.randint(-60, 0)
            self.rect.left = random.randint(0, SCREEN_WIDTH)
            self.speed_x = random.randint(-2, 2)
            self.speed_y = random.randint(1, 1)
