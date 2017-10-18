import pygame
from pygame.sprite import Sprite
class EnemyBullet(Sprite):
    def __init__(self, setting, alien, screen):
        super(EnemyBullet, self).__init__()
        self.screen = screen

        #initialize the bullet to rect 0,0 and set the width and height
        self.rect = pygame.Rect(0, 0, 1,10)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        self.y = float(self.rect.y)
        self.color = (0,255,0)
        self.speed = setting.bullet_speed

    def update(self):
        #moving the bullet forward
        self.y += 2
        #changing the bullet's position
        self.rect.y = self.y
        # print(self.rect.y)

    def draw_enemybullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

