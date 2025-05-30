import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character movement")

f = pygame.font.Font(None, 36)

brick_group = pygame.sprite.Group()

paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(600, 500)



gameloop = True
FPS = 30
clock = pygame.time.Clock()

while gameloop:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    
    st = f.render("Score: "+str(paddle.score), True, "blue")
    str1 = st.get_rect(x = WIDTH//2, y = 30)
    screen.blit(st, str1)

    st1 = f.render("Lives: "+str(paddle.lives), True, "blue")
    str2 = st1.get_rect(x = WIDTH //3, y = 30)
    screen.blit(st1, str2)

    pygame.draw.line(screen, "white", (0, 60), (1200, 60))
    pygame.draw.line(screen, "white", (0,590), (1200, 590))

    paddle.update(event)

    paddle.draw(screen)

    ball.update()

    ball.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit