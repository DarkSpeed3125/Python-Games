import pygame
from nanobot import Nanobot
from bacteria import Bacteria

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character movement")

nano_group=pygame.sprite.Group()
nano_laser_group = pygame.sprite.Group()
nano = Nanobot(nano_laser_group)
nano_group.add(nano)
bacteria_group = pygame.sprite.Group()
bacteria_laser_group = pygame.sprite.Group()

f = pygame.font.Font(None, 36)

gameloop = True
FPS = 30
clock = pygame.time.Clock()
gameover = False
gamewin = False

nr = 5
nc = 11
sx = 100
sy = 50
xspace = 100
yspace = 70

bacteria_fire = pygame.mixer.Sound("Nanocillium Game/bacteria_fire.wav")
gamewin_sound = pygame.mixer.Sound("Nanocillium Game/game_win.mp3")
breach_sound = pygame.mixer.Sound("Nanocillium Game/breach.wav")
gameover_sound = pygame.mixer.Sound("Nanocillium Game/game_over.mp3")
enemyhit_sound = pygame.mixer.Sound("Nanocillium Game/game_over.wav")




for row in range(nr):
    for column in range(nc):
        x = sx + column * xspace
        y = sy + row * yspace
        bact = Bacteria(x, y, 2, bacteria_laser_group, bacteria_group)
        bacteria_group.add(bact)

while gameloop:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nano.fire()
    
    st = f.render("Score: "+str(nano.score), True, "blue")
    str1 = st.get_rect(x = WIDTH//2, y = 30)
    screen.blit(st, str1)

    st1 = f.render("Lives: "+str(nano.lives), True, "blue")
    str2 = st1.get_rect(x = WIDTH //3, y = 30)
    screen.blit(st1, str2)

    for bacteria in bacteria_group:
        if bacteria.rect.bottom > 580 or nano.lives == 0:
            st2 = f.render("Bacteria Breached!" , True, "white")
            str3 = st2.get_rect(x = WIDTH/2, y = 350)
            gameover = True

    if gameover == True:
        screen.fill("black")
        screen.blit(st2, str3)
        pygame.display.update()
        gameover_sound.play()
        pygame.time.delay(2000)
        gameloop = False

    if len(bacteria_group) == 0:
        st3 = f.render("COngratulations! You win!", True, "white")
        str4 = st3.get_rect(x = WIDTH/2, y = 350)
        gamewin = True

    if gamewin == True:
        screen.fill("black")
        screen.blit(st3, str4)
        pygame.display.update()
        gamewin_sound.play()
        pygame.time.delay(2000)
        gameloop = False

    

    pygame.draw.line(screen, "white", (0, 60), (1200, 60))
    pygame.draw.line(screen, "white", (0,590), (1200, 590))

    if pygame.sprite.groupcollide(nano_laser_group, bacteria_group, True, True):
        nano.score = nano.score + 100
        enemyhit_sound.play()


    if pygame.sprite.spritecollide(nano, bacteria_laser_group, True):
        nano.lives = nano.lives - 1
        breach_sound.play()

    nano_group.update(event)

    nano_group.draw(screen)

    nano_laser_group.update()

    nano_laser_group.draw(screen)

    bacteria_group.update()

    bacteria_group.draw(screen)

    bacteria_laser_group.update()

    bacteria_laser_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()