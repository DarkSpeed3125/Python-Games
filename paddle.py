import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.image = pygame.image.load("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/The Brick Game/PaddleImage.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height
        self.velocity = 10
        self.score = 0
        self.lives = 0

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x = self.rect.x - self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x = self.rect.x + self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)