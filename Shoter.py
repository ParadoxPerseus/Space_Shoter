import time
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
explosion_music = pygame.mixer.Sound('zvuk-vzryva2.mp3')
music = pygame.mixer.Sound('2-jungle-hangar-stages-1-7.mp3')
explosion_image_dict = {}
explosion_image_dict['small'] = []
explosion_image_dict['large'] = []
explosion_image_dict['tiny'] = []
explosion_image_dict['medium'] = []
for i in range(9):
    file_name = 'regularExplosion0' + str(i) + '.png'
    explosion_image = pygame.image.load(file_name).convert()
    explosion_image.set_colorkey(BLACK)
    large_image = pygame.transform.scale(explosion_image, (40, 40))
    explosion_image_dict['large'].append(large_image)
    small_image = pygame.transform.scale(explosion_image, (20, 20))
    explosion_image_dict['small'].append(small_image)
    medium_image = pygame.transform.scale(explosion_image, (80, 80))
    explosion_image_dict['medium'].append(medium_image)
    tiny_image = pygame.transform.scale(explosion_image, (10, 10))
    explosion_image_dict['tiny'].append(tiny_image)
bonus_image_dict = {}
bonus_image_dict['hp'] = pygame.image.load('pill_green.png').convert()
bonus_image_dict['gun'] = pygame.image.load('bolt_gold.png').convert()
bonus_image_dict['shield'] = pygame.image.load('shield_bronze.png').convert()
bonus_image_dict['star'] = pygame.image.load('star_gold.png').convert()
ship = Ship()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)
bullets = pygame.sprite.Group()
bonuses = pygame.sprite.Group()
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
music.play()
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
            shot_music = pygame.mixer.Sound('выстрел.mp3')
            shot_music.play()
            if ship.bonus_gun:
                bullet = Bullet(ship.rect.centerx, ship.rect.top)
                bullets.add(bullet)
                all_sprites.add(bullet)
                bullet2 = Bullet(ship.rect.left, ship.rect.centery)
                bullets.add(bullet2)
                all_sprites.add(bullet2)
                bullet1 = Bullet(ship.rect.right, ship.rect.centery)
                bullets.add(bullet1)
                all_sprites.add(bullet1)
            else:
                bullet = Bullet(ship.rect.centerx, ship.rect.top)
                bullets.add(bullet)
                all_sprites.add(bullet)
    player_meteor_hit = pygame.sprite.spritecollide(ship, meteors, True, pygame.sprite.collide_circle)
    for hit in player_meteor_hit:
        if hit.radius >= 40:
            explosion_music.play()
            ship.xp -= 50
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        elif hit.radius < 17.2 and hit.radius >= 17.2:
            explosion_music.play()
            ship.xp -= 25
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            explosion_music.play()
            all_sprites.add(explosion)
        elif hit.radius < 17.2 and hit.radius > 11.2:
            explosion_music.play()
            ship.xp -= 10
            explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
            all_sprites.add(explosion)
        else:
            explosion_music.play()
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
        if random.random() > 0.1:
            bonus = Bonus(bonus_image_dict, hit.rect.center)
            bonuses.add(bonus)
            all_sprites.add(bonus)
        else:
            if hit.radius > 35:
                explosion = Explosion(explosion_image_dict, hit.rect.center, 'medium')
                all_sprites.add(explosion)
                explosion_music.play()
            if hit.radius < 17 and hit.radius >= 1:
                explosion = Explosion(explosion_image_dict, hit.rect.center, 'tiny')
                all_sprites.add(explosion)
                explosion_music.play()
            if hit.radius > 11:
                explosion = Explosion(explosion_image_dict, hit.rect.center, 'small')
                all_sprites.add(explosion)
                explosion_music.play()
            if hit.radius < 75 and hit.radius >= 79:
                explosion = Explosion(explosion_image_dict, hit.rect.center, 'large')
                all_sprites.add(explosion)
                explosion_music.play()
        if hit.radius >= 40:
            score += 1
        elif hit.radius < 17.2 and hit.radius >= 17.2:
            score += 2
        elif hit.radius < 17.2 and hit.radius > 11.2:
            score += 3
        elif hit.radius < 8.6 and hit.radius > 4.3:
            score += 5
    player_hit_bonus = pygame.sprite.spritecollide(ship, bonuses, True, pygame.sprite.collide_circle)
    for hit in player_hit_bonus:
        if hit.type == 'hp':
            ship.xp += random.randint(20, 50)
            if ship.xp > 100:
                ship.xp = 100
        if hit.type == 'gun':
            ship.bonus_gun = True
        if hit.type == 'shield':
            pass
        if hit.type == 'star':
            pass

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
