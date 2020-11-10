import sys, pygame
import random

class multiLevelTiming:
    BLUE = (40, 40, 200)
    RED = (240, 50, 50)
    GREEN = (70, 200, 20)
    BLACK = (0, 0, 0)
    BOXX = 50
    BOXDIST = 200
    BOXY = [i for i in range(100, 600, BOXDIST)]
    BOXWIDTH = 500
    BOXHEIGHT = 60

    START = BOXX
    STOP = BOXX + BOXWIDTH
    tickerPos = START
    tickerYPos = BOXY[0] - 15
    TICKERWIDTH = 15
    TICKERHEIGHT = BOXHEIGHT + 30
    TOTALBOXES = 3
    TICKERSPEEDMODIFIER = 3
    tickerSpeed = 25
    currentBox = 0
    winWindow = 100

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        size = [600, 600]
        self.screen = pygame.display.set_mode(size)


    def winDims(self, window):
        return random.randint(self.BOXX, self.BOXX + self.BOXWIDTH - window)



    def gameLoop(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        ruleTextsurface = myfont.render('Click in green square', False, (120, 120, 210))
        winTextsurface = myfont.render('YOU WIN!', False, (255, 255, 210))

        win = False

        shownBoxes = [[self.BOXX, self.BOXY[0], self.BOXWIDTH, self.BOXHEIGHT]]
        winStart = self.winDims(self.winWindow)
        greenBoxes = [[winStart, self.BOXY[0], self.winWindow, self.BOXHEIGHT]]

        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print('clicked')
                    if win:
                        continue

                    if self.tickerPos > winStart and self.tickerPos < winStart + self.winWindow:
                        print('INSIDE')
                        self.currentBox += 1

                        if self.currentBox == self.TOTALBOXES:
                            win = True
                            continue

                        self.tickerYPos += self.BOXDIST
                        shownBoxes.append([self.BOXX, self.BOXY[self.currentBox], self.BOXWIDTH, self.BOXHEIGHT])
                        winWindow = int(self.winWindow / 1.5)
                        if self.tickerSpeed > 0:
                            self.tickerSpeed += self.TICKERSPEEDMODIFIER

                        else:
                            self.tickerSpeed -= self.TICKERSPEEDMODIFIER

                        winStart = self.winDims(winWindow)
                        greenBoxes.append([winStart, self.BOXY[self.currentBox], winWindow, self.BOXHEIGHT])

            self.tickerPos += self.tickerSpeed

            if self.tickerPos > self.STOP or self.tickerPos < self.START:
                self.tickerSpeed *= -1

            ticker = [self.tickerPos, self.tickerYPos, self.TICKERWIDTH, self.TICKERHEIGHT]

            for box in range(len(shownBoxes)):
                pygame.draw.rect(self.screen, self.BLUE, shownBoxes[box], 3)
                pygame.draw.rect(self.screen, self.GREEN, greenBoxes[box])

            pygame.draw.rect(self.screen, self.RED, ticker)
            #
            self.screen.blit(ruleTextsurface, (0, 50))

            if win:
                self.screen.blit(winTextsurface, (300, 50))
            pygame.display.flip()
            self.screen.fill(self.BLACK)


if __name__ == '__main__':
    game = multiLevelTiming()
    game.gameLoop()