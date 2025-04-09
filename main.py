import pygame
from paddle import Paddle

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character movement")

paddle = Paddle(WIDTH, HEIGHT)

gameloop = True
FPS = 30
clock = pygame.time.Clock()

while gameloop:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    paddle.update(event)

    paddle.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit