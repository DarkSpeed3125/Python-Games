import pygame
from nanobot_laser import Nanobot_Laser

WIDTH = 1200
HEIGHT = 700

class Nanobot(pygame.sprite.Sprite):
    def __init__(self, laser_group):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/Nanocillium Game/NanoBotImage.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT
        self.velocity = 10
        self.laser_group = laser_group
        self.score = 0
        self.lives = 5

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x = self.rect.x - self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x = self.rect.x + self.velocity

    def fire(self):
        if len(self.laser_group) < 2:
            Nanobot_Laser(self.rect.centerx, self.rect.top, self.laser_group)

     



    