import sys,pygame

pygame.init()

clock=pygame.time.Clock()
size = [600, 600]
screen = pygame.display.set_mode(size)

BLUE = (40, 40, 200)
RED = (240, 50, 50)
GREEN = (70, 200, 20)
BLACK = (0,0,0)
START = 50
STOP = 250
WINSTART = 100
WINEND = 150
tickerPos = START

tickerSpeed = 5

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

ruleTextsurface = myfont.render('Click in green square', False, (120, 60, 210))
winTextsurface = myfont.render('YOU WIN!', False, (120, 120, 210))

win = False

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            print('clicked')
            if tickerPos > WINSTART and tickerPos < WINEND:
                win = True

    tickerPos += tickerSpeed

    if tickerPos > STOP or tickerPos < START:
        tickerSpeed *= -1

    boxDims = [50,200, 200, 50]
    greenZoneDims = [WINSTART, 200, WINEND - WINSTART, 50]
    ticker = [tickerPos, 180, 10, 90]

    pygame.draw.rect(screen, BLUE, boxDims, 3)
    pygame.draw.rect(screen, GREEN, greenZoneDims)
    pygame.draw.rect(screen, RED, ticker)
    #
    screen.blit(ruleTextsurface, (0, 60))
    if win:
        screen.blit(winTextsurface, (300, 100))
    pygame.display.flip()
    screen.fill(BLACK)
