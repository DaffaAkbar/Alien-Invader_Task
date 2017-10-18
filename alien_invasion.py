import pygame
from setting import Setting
from pygame.sprite import Group
from ship import Ship
from Alien import Alien
from game_stats import GameStats
from game_functions import *
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode([setting.width,setting.height])

    #Now create the object of the ship
    ship = Ship(screen, setting)
    pygame.display.set_caption("Alien Games")

    # Make the Play button
    play_button = Button(setting, screen, "Play")

    #create an instance of gameStats
    stats = GameStats(setting,screen,ship)
    sb = Scoreboard(setting, screen, stats)

    #store a bullet in a list
    bullets = Group()
    enemybullets=Group()
    aliens = Group()
    create_fleet(setting, screen, aliens, ship)

    while True:
        check_event(setting, screen, stats, play_button, sb, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            update_bullet(setting, screen, stats, sb, ship, bullets, aliens)
            for alien in aliens:
                fire_enemybullet(alien,setting,screen,enemybullets)
            update_enemybullet(setting, screen, stats, sb, ship, enemybullets, aliens)
            update_alien(setting, stats, screen, ship, aliens, bullets,)
        update_screen(screen,setting, sb, ship, stats, bullets, aliens, play_button,enemybullets)


run_game()