import random
import pygame
from explosion import Explosion
from meteor import Meteor
from ship import Ship
from bonus import Bonus
from const import *
from bullet import Bullet
import sys

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.image.load('purple.png').convert()

file = ['meteorGrey_big1.png', 'meteorGrey_big2.png', 'meteorGrey_med1.png', 'meteorGrey_med2.png',
        'meteorGrey_small1.png', 'meteorGrey_small2.png', 'meteorGrey_tiny1.png', 'meteorGrey_tiny2.png',
        'meteorGrey_big3.png', 'meteorGrey_big4.png']
images = []
for i in file:
    meteor_image = pygame.image.load(i).convert()
    images.append(meteor_image)

explosion_image_dict = {}
explosion_image_dict['small'] = []
explosion_image_dict['large'] = []
for i in range(9):
    file_name = 'regularExplosion0' + str(i) + '.png'
    explosion_image = pygame.image.load(file_name).convert()
    explosion_image.set_colorkey(BLACK)
    large_image = pygame.transform.scale(explosion_image, (80, 80))
    explosion_image_dict['large'].append(large_image)
    small_image = pygame.transform.scale(explosion_image, (20, 20))
    explosion_image_dict['small'].append(small_image)


ship = Ship()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)
bullets = pygame.sprite.Group()
meteors = pygame.sprite.Group()


def create_meteor(images):
    meteor = Meteor(images)
    all_sprites.add(meteor)
    meteors.add(meteor)


for i in range(20):
    create_meteor(images)


def draw_xp_bar():
    if ship.xp < 0:
        ship.xp = 0
    fill = (ship.xp / 100) * XP_BAR_WIDTH
    outline_rect = pygame.Rect(SCREEN_WIDTH - XP_BAR_WIDTH - 10, 10, XP_BAR_WIDTH, 15)
    fill_rect = pygame.Rect(SCREEN_WIDTH - XP_BAR_WIDTH - 10, 10, fill, 15)
    pygame.draw.rect(window, WHITE2, fill_rect)
    pygame.draw.rect(window, WHITE, outline_rect, 2)


score = 0

text = pygame.font.Font('DS-DIGIT.TTF', 32)


pygame.display.set_caption('PYGAME')
pygame.display.set_icon(pygame.image.load('logo.png'))
clock = pygame.time.Clock()
lives = 5

while True:
    text_score = str(score)
    text_score_render = text.render('SCORE:' + text_score, True, YELLOW)
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
        if hit.radius >= 40:
            ship.xp -= 50
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        elif hit.radius < 17.2 and hit.radius >= 17.2:
            ship.xp -= 25
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        elif hit.radius < 17.2 and hit.radius > 11.2:
            ship.xp -= 10
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        else:
            ship.xp -= 5
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        if ship.xp <= 0:
            pygame.quit()
            sys.exit()
        create_meteor(images)
    bullets_hit_meteors = pygame.sprite.groupcollide(meteors, bullets, True, True,
                                                     pygame.sprite.collide_circle)
    for hit in bullets_hit_meteors:
        create_meteor(images)
        if hit.radius > 35:
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        if hit.radius < 17 and hit.radius >= 11:
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'small')
            all_sprites.add(explosion)
        if hit.radius >= 40:
            score += 1
        elif hit.radius < 17.2 and hit.radius >= 17.2:
            score += 2
        elif hit.radius < 17.2 and hit.radius > 11.2:
            score += 3
        elif hit.radius < 8.6 and hit.radius > 4.3:
            score += 5
        a = random.randint(0, 10)
        bonuses = pygame.sprite.Group()
        if a == 10:
            bonus = Bonus()
            bonuses.add(bonus)
            all_sprites.add(bonus)
    # window.fill(BLACK)
    window.blit(bg, (0, 0))
    all_sprites.draw(window)
    all_sprites.update()
    meteors.update()
    window.blit(text_score_render, (5, 5))
    draw_xp_bar()
    if ship.xp < 20:
        WHITE2 = RED
    pygame.display.update()
