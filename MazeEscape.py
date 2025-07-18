import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

display = pygame.display.set_mode((600,600))
pygame.display.set_caption("Maze Escape")

Gameloop = True
FPS = 30
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0,981)
draw_options = pymunk.pygame_util.DrawOptions(display)

Gameover = False

def create_ball(space, position):
    body = pymunk.Body(1,pymunk.moment_for_circle(1, 0, 20))
    body.position = (position)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0
    space.add(body, shape)
    return(body,shape)

ball_body,ball = create_ball(space, (100,500))

def create_platform(space, position, width, height):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (position)
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.elasticity = 0.8
    shape.friction = 0
    space.add(body, shape)
    return(body,shape)



base = create_platform(space, (300,550), 500, 20)
platform_a = create_platform(space, (100, 450), 100, 20)
platform_b = create_platform(space, (350,450), 200, 20)
platform_c = create_platform(space, (150,350), 100, 20)
platform_d = create_platform(space, (355,350), 100, 20)
platform_e = create_platform(space, (550,350), 100, 20)
platform_f = create_platform(space, (50,250), 150, 20)
platform_g = create_platform(space, (500,250), 150, 20)
platform_h = create_platform(space, (250,150), 150, 20)
platform_i = create_platform(space, (550,150), 150, 20)
platform_j = create_platform(space, (300,250), 150, 20)

exit = pygame.draw.rect(display, "green", (550, 50, 50, 75))

font = pygame.font.SysFont("Comic Sans MS", 20)


while Gameloop:
    
    display.fill("black")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Gameloop = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ball_body.position += pymunk.Vec2d(5, 0)
        if event.key == pygame.K_LEFT:
            ball_body.position += pymunk.Vec2d(-5, 0)
        if event.key == pygame.K_UP:
            ball_body.position += pymunk.Vec2d(0, -10)

    if ball_body.position.x > 610 or ball_body.position.x < 0:
        Gameover = True

    if Gameover == True:
        display.fill("black")

        go = font.render("Game Over!", True, "red")
        gt = go.get_rect(center = (300,300))
        display.blit(go,gt)

        pygame.display.update()
        pygame.time.delay(3000)
        Gameloop =  False
    

    if ball_body.position.x == 560:
        display.fill("black")
        gw = font.render("You Won!", True, "blue")
        gp = gw.get_rect(center = (300,300))
        display.blit(gw,gp)

        pygame.display.update()
        pygame.time.delay(3000)
        Gameloop = False


    space.step(1/60)
    space.debug_draw(draw_options)
    exit = pygame.draw.rect(display, "green", (550, 50, 50, 77))

    


    pygame.display.update()
    clock.tick(FPS)


pygame.quit