import pygame
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

speed_x = 1
speed_y = 1

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/The Brick Game/ballImage.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 10
        self.direction = 1

    def update(self):
            self.rect.y = self.rect.y - self.velocity * self.direction


            if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
                self.speed_x *= -1
            if self.rect.top <=0 or self.rect.bottom >= WINDOW_HEIGHT:
                self.speed_y *= -1


    def draw(self, screen):
         screen.blit(self.image, self.rect)