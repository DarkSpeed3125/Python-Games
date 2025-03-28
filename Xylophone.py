import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

BAR1_HEIGHT = 200
BAR1_WIDTH = 100
MALLET_SIZE = 30

mallet_x = 280
mallet_y = 50

mallet_dx = 0
mallet_dy = 0

speed = 10
malletposition = mallet_x, mallet_y, MALLET_SIZE, MALLET_SIZE

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xylophone")

display.fill("black")
bar1 = pygame.draw.rect(display, "red", (0, 50, 70, 200))
bar2 = pygame.draw.rect(display, "orange", (80, 50, 70, 180))
bar3 = pygame.draw.rect(display, "yellow", (160, 50, 70, 160))
bar4 = pygame.draw.rect(display, "green", (240, 50, 70, 140))
bar5 = pygame.draw.rect(display, "cyan", (320, 50, 70, 120))
bar6 = pygame.draw.rect(display, "purple", (400, 50, 70, 100))
bar7 = pygame.draw.rect(display, "red", (480, 50, 70, 80))
mallet = pygame.draw.rect(display, "white", (mallet_x, mallet_y, MALLET_SIZE, MALLET_SIZE))

FPS = 30
clock = pygame.time.Clock()

gameloop = True

note1 = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/note1.mp3")
note2 = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/note2.mp3")
note3 = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/note3.mp3")
noteA = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/noteA.mp3")
noteB = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/noteB.mp3")
noteC = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/noteC.mp3")
noteD = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/noteD.mp3")
noteE = pygame.mixer.Sound("C:/Users/Lenny R Johnson/OneDrive/Desktop/Python Games/noteE.mp3")

while gameloop == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    if mallet.colliderect(bar1):
        x = note1
    if mallet.colliderect(bar2):
        x = note2
    if mallet.colliderect(bar3):
        x = note3
    if mallet.colliderect(bar4):
        x = noteA
    if mallet.colliderect(bar5):
        x = noteB
    if mallet.colliderect(bar6):
        x = noteC
    if mallet.colliderect(bar7):
        x = noteD

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            mallet_dx = 0
            mallet_dy = -1*speed
        elif event.key == pygame.K_DOWN:
            mallet_dx = 0
            mallet_dy = 1*speed
        elif event.key == pygame.K_LEFT:
            mallet_dx = -1*speed
            mallet_dy = 0
        elif event.key == pygame.K_RIGHT:
            mallet_dx = 1*speed
            mallet_dy = 0
        elif event.key == pygame.K_q:
            x.play()
    
        
    
    mallet_x += mallet_dx
    mallet_y += mallet_dy

    malletposition = mallet_x, mallet_y, MALLET_SIZE, MALLET_SIZE

    display.fill("black")
    bar1 = pygame.draw.rect(display, "red", (0, 50, 70, 200))
    bar2 = pygame.draw.rect(display, "orange", (80, 50, 70, 180))
    bar3 = pygame.draw.rect(display, "yellow", (160, 50, 70, 160))
    bar4 = pygame.draw.rect(display, "green", (240, 50, 70, 140))
    bar5 = pygame.draw.rect(display, "cyan", (320, 50, 70, 120))
    bar6 = pygame.draw.rect(display, "purple", (400, 50, 70, 100))
    bar7 = pygame.draw.rect(display, "red", (480, 50, 70, 80))
    mallet = pygame.draw.rect(display, "white", (mallet_x, mallet_y, MALLET_SIZE, MALLET_SIZE))

    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()