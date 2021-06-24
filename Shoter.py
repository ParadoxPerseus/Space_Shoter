import pygame
from meteor import Meteor
from ship import Ship
from const import *
from bullet import Bullet
import sys

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ship = Ship()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)
bullets = pygame.sprite.Group()
meteors = pygame.sprite.Group()

for i in range(10):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)

pygame.display.set_caption('PYGAME')
pygame.display.set_icon(pygame.image.load('logo.png'))
clock = pygame.time.Clock()
lives = 5

while True:
    text_lives = str(lives)
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bullet = Bullet(ship.rect.centerx, ship.rect.top)
            bullets.add(bullet)
            all_sprites.add(bullet)

    player_meteor_hit = pygame.sprite.spritecollide(ship, meteors, True, pygame.sprite.collide_circle)
    for hit in player_meteor_hit:
        ship.xp -= 10
        if ship.xp <= 0:
            pygame.quit()
            sys.exit()
        meteor = Meteor()
        meteors.add(meteor)
        all_sprites.add(meteor)
    bullets_hit_meteors = pygame.sprite.groupcollide(bullets, meteors, True, True,
                                                     pygame.sprite.collide_circle)
    for hit in bullets_hit_meteors:
        meteor = Meteor()
        meteors.add(meteor)
        all_sprites.add(meteor)
    window.fill(GREEN)
    all_sprites.draw(window)
    all_sprites.update()
    meteors.update()
    pygame.display.update()
