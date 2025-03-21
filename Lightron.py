import pygame
from random import randint

pygame.init()

WIDTH = 600
HEIGHT = 600

TRON_SIZE = 20

head_x = 300
head_y = 300


tron_body = []
tronposition = head_x, head_y, TRON_SIZE, TRON_SIZE
tron_dx = 0
tron_dy = 0

score = 0
speed = 10

FPS = 30
clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tron Lightcycle Game")

gameloop = True

tron = pygame.draw.rect(display, "white",  (head_x, head_y, TRON_SIZE, TRON_SIZE))

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            tron_dx = 0
            tron_dy = -1*speed
        elif event.key == pygame.K_RIGHT:
            tron_dx = 1*speed
            tron_dy = 0
        elif event.key == pygame.K_LEFT:
            tron_dx = -1*speed
            tron_dy = 0
        elif event.key == pygame.K_DOWN:
            tron_dx = 0
            tron_dy = 1*speed

    tron_body.insert(0, tronposition)
    
    tron_body.append(tronposition)



    head_x += tron_dx
    head_y += tron_dy


    head_x += tron_dx
    head_y += tron_dy
    tronposition =(head_x, head_y, TRON_SIZE, TRON_SIZE)

    display.fill("black")
    for trail in tron_body:
        pygame.draw.rect(display, "cyan", trail)
    tron = pygame.draw.rect(display, "white",  (head_x, head_y, TRON_SIZE, TRON_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()