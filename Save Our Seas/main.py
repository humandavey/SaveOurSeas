import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.font.init()

small_font = pygame.font.Font('assets/GAME.ttf', 30)
font = pygame.font.Font('assets/GAME.ttf', 60)
big_font = pygame.font.Font('assets/GAME.ttf', 120)
fps = 60
width, height = 800, 600
game_state = "menu"
clock = pygame.time.Clock()
score = 0
hight_score = 0

select_sound = pygame.mixer.Sound("assets/select.wav")
pickup_sound = pygame.mixer.Sound("assets/pickup.wav")
die_sound = pygame.mixer.Sound("assets/die.wav")

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Save Our Seas")
pygame.display.set_icon(pygame.image.load("assets/icon.png").convert_alpha())

player_surf = pygame.image.load("assets/boat.png").convert_alpha()
player_rect = player_surf.get_rect(center = (100, 300))

background_surf = pygame.image.load("assets/background.png").convert_alpha()

bottle_surf = pygame.image.load("assets/bottle.png").convert_alpha()
bottle_rect = bottle_surf.get_rect(topleft = (random.randint(820, 1500), 0))
bottle_rect.y = random.randint(125, 550)
shoe_surf = pygame.image.load("assets/shoe.png").convert_alpha()
shoe_rect = shoe_surf.get_rect(topleft = (random.randint(820, 1500), 0))
shoe_rect.y = random.randint(125, 550)
bag_surf = pygame.image.load("assets/bag.png").convert_alpha()
bag_rect = bag_surf.get_rect(topleft = (random.randint(820, 1500), 0))
bag_rect.y = random.randint(125, 550)

fish_1_surf = pygame.image.load("assets/fish_1.png").convert_alpha()
fish_1_rect = fish_1_surf.get_rect(center = (random.randint(820, 1500), 0))
fish_1_rect.y = random.randint(125, 550)
fish_2_surf = pygame.image.load("assets/fish_2.png").convert_alpha()
fish_2_rect = fish_2_surf.get_rect(center = (random.randint(820, 1500), 0))
fish_2_rect.y = random.randint(125, 550)

while True:
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "menu":
        screen.blit(background_surf, (0, 0))
        menu_surf = big_font.render("Save Our Seas", False, (0, 0, 0))
        menu_rect = menu_surf.get_rect(center = (400, 230))
        screen.blit(menu_surf, menu_rect)
        author_surf = small_font.render("Made by Relend", False, (0, 0, 0))
        author_rect = author_surf.get_rect(center = (400, 310))
        screen.blit(author_surf, author_rect)
        if keys[pygame.K_SPACE]:
            game_state = "playing"
            pygame.mixer.Sound.play(select_sound)

        # MOUSE CLICKING
        if background_surf.get_rect().collidepoint(mouse_pos) and any(mouse_buttons):
            game_state = "playing"
            pygame.mixer.Sound.play(select_sound)
    elif game_state == "playing":

        screen.blit(background_surf, (0, 0))
        screen.blit(player_surf, player_rect)
        screen.blit(shoe_surf, shoe_rect)
        screen.blit(bag_surf, bag_rect)
        screen.blit(bottle_surf, bottle_rect)
        screen.blit(fish_1_surf, fish_1_rect)
        screen.blit(fish_2_surf, fish_2_rect)
        # UP / DOWN KEYS
        if keys[pygame.K_UP]:
            player_rect.y = player_rect.y-4
        if keys[pygame.K_DOWN]:
            player_rect.y = player_rect.y+4

        # COLLISIONS
        if player_rect.top < 75:
            player_rect.top = 75
        if player_rect.bottom > 600:
            player_rect.bottom = 600

        if shoe_rect.right < 0:
            shoe_rect.y = random.randint(125, 550)
            shoe_rect.x = random.randint(820, 1500)
        if bag_rect.right < 0:
            bag_rect.y = random.randint(125, 550)
            bag_rect.x = random.randint(820, 1500)
        if bottle_rect.right < 0:
            bottle_rect.y = random.randint(125, 550)
            bottle_rect.x = random.randint(820, 1500)
        if fish_1_rect.right < 0:
            fish_1_rect.y = random.randint(125, 550)
            fish_1_rect.x = random.randint(820, 1500)
        if fish_2_rect.right < 0:
            fish_2_rect.y = random.randint(125, 550)
            fish_2_rect.x = random.randint(820, 1500)

        if(player_rect.colliderect(shoe_rect)):
            score = score+100
            shoe_rect.x = -100
            pygame.mixer.Sound.play(pickup_sound)
        if(player_rect.colliderect(bag_rect)):
            score = score+100
            bag_rect.x = -100
            pygame.mixer.Sound.play(pickup_sound)
        if(player_rect.colliderect(bottle_rect)):
            score = score+100
            bottle_rect.x = -100
            pygame.mixer.Sound.play(pickup_sound)
        if(player_rect.colliderect(fish_1_rect)):
            game_state = "dead"
            fish_1_rect.x = -100
            pygame.mixer.Sound.play(die_sound)
        if(player_rect.colliderect(fish_2_rect)):
            game_state = "dead"
            fish_2_rect.x = -100
            pygame.mixer.Sound.play(die_sound)

        # UPDATE POSITIONS
        shoe_rect.x = shoe_rect.x-5
        bag_rect.x = bag_rect.x-5
        bottle_rect.x = bottle_rect.x-5
        fish_1_rect.x = fish_1_rect.x-5
        fish_2_rect.x = fish_2_rect.x-5

        score_surf = font.render("Score: " + str(score), False, (0, 0, 0))
        score_rect = score_surf.get_rect(center = (400, 40))
        screen.blit(score_surf, score_rect)
    elif game_state == "dead":
        screen.blit(background_surf, (0, 0))
        death_surf = big_font.render("YOU DIED!", False, (0, 0, 0))
        death_rect = death_surf.get_rect(center = (400, 230))
        screen.blit(death_surf, death_rect)
        if score > hight_score:
            hight_score = score
        high_score_surf = font.render("High Score: " + str(hight_score), False, (0, 0, 0))
        high_score_rect = high_score_surf.get_rect(center = (400, 290))
        screen.blit(high_score_surf, high_score_rect)
        if background_surf.get_rect().collidepoint(mouse_pos) and any(mouse_buttons):
            game_state = "playing"
            pygame.mixer.Sound.play(select_sound)
        if keys[pygame.K_SPACE]:
            game_state = "playing"
            pygame.mixer.Sound.play(select_sound)
        score = 0
    else:
        screen.fill("#ff0000")
    pygame.display.flip()
    clock.tick(fps)

# boat moves right
# you control y-axis
#
# try to dodge fish
# obstacles
#
# collect trash along
# the way to get points
