import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

display = pygame.display.set_mode((600,600))
pygame.display.set_caption("Bouncy Ball")

gameloop = True
FPS = 30
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0,981)
draw_options = pymunk.pygame_util.DrawOptions(display)

def create_ball(space, position, elasticity):
    body = pymunk.Body(1,pymunk.moment_for_circle(1, 0, 20))
    body.position = (position)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = elasticity
    space.add(body, shape)
    return(body,shape)

ball_body1,ball1 = create_ball(space, (100, 200), 0.8)
ball_body2,ball2 = create_ball(space, (300, 200), 0.3)
ball_body3,ball3 = create_ball(space, (500, 200), 0.5)

b0 = space.static_body
segment = pymunk.Segment(b0, (0,500), (600, 500), 4)
segment.elasticity = 1.0
space.add(segment)

while gameloop:
    
    display.fill("black")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    space.step(1/60)
    space.debug_draw(draw_options)


    


    pygame.display.update()
    clock.tick(FPS)


pygame.quit

