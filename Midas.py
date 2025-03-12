import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

MIDAS_SIZE = 20
OBJECT_SIZE = 20

head_x = 300
head_y = 300

midas_dx = 0
midas_dy = 0

score = 0
speed = 10

FPS = 30
clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hand Of Midas Game")

gameloop = True

object_color = "red"
object2_color = "blue"
object3_color = "orange"
object4_color = "purple"

midas = pygame.draw.rect(display, "lime",  (head_x, head_y, MIDAS_SIZE, MIDAS_SIZE))
objectposition = (500, 500, OBJECT_SIZE, OBJECT_SIZE)
object2position = (500, 200, OBJECT_SIZE, OBJECT_SIZE)
object3position = (200, 500, OBJECT_SIZE, OBJECT_SIZE)
object4position = (200, 200, OBJECT_SIZE, OBJECT_SIZE)
object = pygame.draw.rect(display, object_color, objectposition)
object2 = pygame.draw.rect(display, object_color, object2position)
object3 = pygame.draw.rect(display, object_color, object3position)
object4 = pygame.draw.rect(display, object_color, object4position)

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            midas_dx = 0
            midas_dy = -1*speed
        elif event.key == pygame.K_RIGHT:
            midas_dx = 1*speed
            midas_dy = 0
        elif event.key == pygame.K_LEFT:
            midas_dx = -1*speed
            midas_dy = 0
        elif event.key == pygame.K_DOWN:
            midas_dx = 0
            midas_dy = 1*speed

    head_x += midas_dx
    head_y += midas_dy

    if midas.colliderect(object):
        object_color = "GOLD"

    if midas.colliderect(object2):
        object2_color = "GOLD"

    if midas.colliderect(object3):
        object3_color = "GOLD"

    if midas.colliderect(object4):
        object4_color = "GOLD"

    display.fill("white")
    midas = pygame.draw.rect(display, "lime",  (head_x, head_y, MIDAS_SIZE, MIDAS_SIZE))
    object = pygame.draw.rect(display, object_color, objectposition)
    object2 = pygame.draw.rect(display, object2_color, object2position)
    object3 = pygame.draw.rect(display, object3_color, object3position)
    object4 = pygame.draw.rect(display, object4_color, object4position)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()