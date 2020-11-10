import pygame, sys
import random
import time

pygame.init()
clock = pygame.time.Clock()
size = [800, 800]
screen = pygame.display.set_mode(size)

BLUE = (40, 40, 200)
RED = (240, 50, 50)
GREEN = (70, 200, 20)
BLACK = (0,0,0)
ONSCREEN = 31
RESULTX = 30
RESULTY = 700

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

RedNums = [myfont.render(str(i), False, RED) for i in range(10)]
GreenNums = [myfont.render(str(i), False, GREEN) for i in range(10)]
BlueNums = [myfont.render(str(i), False, BLUE) for i in range(10)]
winTextsurface = myfont.render('YOU WIN!', False, (120, 120, 210))

sequence = [random.randint(0, 9) for i in range(4)]
print(sequence)

shownStack = []
qpos = 0

guessStack = []
guesssTextPos = RESULTX
guess = 10
key = 0
mode = "Play"

while 1:
    # pygame.time.wait(2)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

        if event.type == pygame.KEYUP:
            pressed = chr(key.index(1))
            if pressed.isdigit():
                guess = int(pressed)

    if mode == "Play":
        randx = random.randint(30, 750)
        randy = random.randint(30, 550)
        randNum = random.randint(0, 9)

        if len(shownStack) <= qpos:
            shownStack.append(0)

        if randNum == sequence[0]:
            shownStack[qpos] = GreenNums[randNum], (randx, randy)
        else:
            shownStack[qpos] = RedNums[randNum], (randx, randy)

        qpos += 1
        qpos %= ONSCREEN

        if guess == sequence[0]:
            guessStack.append((BlueNums[guess] , (guesssTextPos, RESULTY)))
            sequence = sequence[1:]
            guesssTextPos += 60
            guess = 10

        for num in shownStack:
            screen.blit(num[0], num[1])

        for num in guessStack:
            screen.blit(num[0], num[1])

        if len(sequence) == 0:
            mode = "DONE"

    else:
        screen.blit(winTextsurface, (300, 100))

    pygame.display.flip()
    screen.fill(BLACK)
