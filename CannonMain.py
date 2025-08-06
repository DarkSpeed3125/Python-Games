import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Cannon Game")

FPS = 60
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0,981)
draw_options = pymunk.pygame_util.DrawOptions(display)

Cannon1 = pygame.image.load("Cannon Game/canon.png")
Cannon1 = pygame.transform.scale(Cannon1, (150,150))

CannonBall1 = pygame.image.load("Cannon Game/cannon_ball.png")
CannonBall1 = pygame.transform.scale(CannonBall1, (40,40)
)
background_image = pygame.image.load("Cannon Game/bg4.jpg")
background_image = pygame.transform.scale(background_image, (800, 600))

def create_cannon(x, y):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (x,y)
    shape = pymunk.Poly.create_box(body, (60,60))
    space.add(body, shape)
    return(body, shape)

Cannon_body, Cannon = create_cannon(50, 450)

def create_cannonball(x, y):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = (x,y)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.2
    shape.friction = 0.2
    space.add(body, shape)
    return(body, shape)

CannonBall_body, CannonBall = create_cannonball(50, 450)

def draw_objects():
    display.blit(background_image, (0,0))

    cannonball_pos = CannonBall_body.position
    display.blit(CannonBall1, (cannonball_pos.x, cannonball_pos.y))

    cannon_pos = Cannon_body.position
    display.blit(Cannon1, (cannon_pos.x, cannon_pos.y))

ground = pymunk.Body(body_type = pymunk.Body.STATIC)
ground_shape = pymunk.Segment(ground, (0, 580), (800, 590), 5)
ground.friction = 0.3
space.add(ground, ground_shape)

Gameloop = True
while Gameloop:

    display.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Gameloop = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            CannonBall_body.position = (150,500)
            x_velocity = (mouse_pos[0]- 150) * 4
            y_velocity = (mouse_pos[1] - 500) * 4
            CannonBall_body.velocity = (x_velocity, y_velocity)

    space.step(1/60)
    draw_objects()


    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit

