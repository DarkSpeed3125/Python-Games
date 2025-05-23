import pygame
from bacteria_laser import Bacteria_laser
import random

WIDTH = 1200

class Bacteria(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, laser_group, bacteria_group):
        super().__init__()
        self.image = pygame.image.load("Nanocillium Game/bacteria.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = 1
        self.velocity = velocity
        self.laser_group = laser_group
        self.bacteria_group = bacteria_group
        
    def update(self):
        self.rect.x = self.rect.x + self.velocity * self.direction

        if self.rect.left < 0 or self.rect.right > WIDTH:
            for bacteria in self.bacteria_group:
               bacteria.direction = bacteria.direction*-1
               bacteria.rect.y = bacteria.rect.y +20

        if random.randint(0,1000) > 999 and len(self.laser_group) > 3:
            self.fire()

    def fire(self):
        Bacteria_laser(self.rect.centerx, self.rect.bottom, self.laser_group)


        

        