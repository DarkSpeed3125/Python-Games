import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brick_group):
        super().__init__()
        bricks = []
        self.image = pygame.transform.scale(self.image, (80,20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.brick_group = brick_group

        