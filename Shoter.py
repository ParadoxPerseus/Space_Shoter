import pygame
from meteor import Meteor
from ship import Ship
from const import *
import sys

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ship = Ship()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)
meteors = pygame.sprite.Group()

for i in range(10):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)

pygame.display.set_caption('PYGAME')

pygame.display.set_icon(pygame.image.load('logo.png'))
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player_meteor_hit = pygame.sprite.spritecollide(ship, meteors, True)
    if len(player_meteor_hit) > 0:
        pygame.quit()
        sys.exit()
    window.fill(GREEN)
    all_sprites.draw(window)
    all_sprites.update()
    meteors.update()
    pygame.display.update()
