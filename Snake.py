import pygame

pygame.init()

display = pygame.display.set_mode((600,600))
pygame.display.set_caption("Classic Snake Game")

gameloop = True

snake = pygame.draw.rect(display, "lime",  (300, 300, 30, 20))

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    
    display.fill("black")
    snake = pygame.draw.rect(display, "lime",  (300, 300, 30, 20))
    pygame.display.flip()

pygame.quit()