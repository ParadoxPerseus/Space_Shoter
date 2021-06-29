import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, image_list, center):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_delay = 50
        self.timer = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.timer > self.frame_delay:
            self.timer = now
            self.frame += 1
            if self.frame < 9:
                old_center = self.rect.center
                self.image = self.image_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = old_center
            else:
                self.kill()
