import pygame

pygame.init()

display = pygame.display.set_mode((600,600))
pygame.display.set_caption("Initials")

gameloop = True

line1 = pygame.draw.rect(display, "lime", (180, 200, 200, 10))
line2 = pygame.draw.rect(display, "lime", (300, 200, 10, 200))
line3 = pygame.draw.rect(display, "lime", (210, 400, 100, 10))

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    
    display.fill("black")
    line1 = pygame.draw.rect(display, "lime", (180, 200, 200, 10))
    line2 = pygame.draw.rect(display, "lime", (300, 200, 10, 200))
    line3 = pygame.draw.rect(display, "lime", (210, 400, 100, 10))
    pygame.display.flip()

pygame.quit()