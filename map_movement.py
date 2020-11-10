import time
import sys, pygame
import random


class constants:
    # pyagme related
    WINDOWWIDTH = 900
    WINDOWHEIGHT = 700

    # Game Length related
    GROUND = 50
    GAMESPEED = 0.2

    # Colors
    BLACK = (0, 0, 0)
    RED = (250, 0, 0)
    BLUE = (0, 0, 200)
    BROWN = (66, 22, 14)
    GRAY = (120, 120, 120)
    LIGHTBLUE = (120, 120, 210)

    # Lasers
    LASERHEIGHT = 10
    LASERSPEED = 5
    LASERS = 3
    LASERSTART = 200

    # Keymap
    LEFTARROW = 276
    UPARROW = 273
    RIGHTARROW = 275
    DOWNARROW = 274

    #MOVEZONE
    MOVEZONEX = 50
    MOVEZONEY = 20
    MOVEZONEWIDTH = 800
    MOVEZONEHEIGHT = 400


    # Player
    PLAYERX = int(WINDOWWIDTH/2)
    PLAYERY = int(WINDOWHEIGHT/2)
    PLAYERWIDTH = 40
    PLAYERHEIGHT = 80
    PLAYERSPEED = 5

    # Rope
    ROPEWIDTH = 5

class rectangle:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, x=0, y=0, w=0, h=0):
        self.setDims(x, y, w, h)

    def setDims(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def boxDims(self):
        return [self.x, self.y, self.width, self.height]


class Player(rectangle):
    SPEED = constants.PLAYERSPEED

    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = constants.PLAYERWIDTH
        self.height = constants.PLAYERWIDTH

        self.center = (int((x + self.width)/2), (int((self.y + self.height)/2)))
        self.radius = int((self.width - self.x)/2)

    def stopMovement(self):
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False


class RopeGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        size = [constants.WINDOWWIDTH, constants.WINDOWHEIGHT]
        self.screen = pygame.display.set_mode(size)
        self.myfont = pygame.font.SysFont('Georgia', 30)

        self.player = Player(constants.PLAYERX, constants.PLAYERY)
        self.walls = []

        self.gameSetup()

    def gameSetup(self):
        wall = rectangle(20,40,120,60)
        self.walls.append(wall)

        wall = rectangle(80,540,10,600)
        self.walls.append(wall)

        wall = rectangle(650,140,40,800)
        self.walls.append(wall)

        pass

    @staticmethod
    def testCollision(box, obstacle):
        boxX = box[0]
        boxY = box[1]
        boxW = box[2]
        boxH = box[3]
        boxR = boxX + boxW
        boxB = boxY + boxH

        obstacleX = obstacle[0]
        obstacleY = obstacle[1]
        obstacleW = obstacle[2]
        obstacleH = obstacle[3]
        obstacleR = obstacleX + obstacleW
        obstacleB = obstacleY + obstacleH

        if boxB > obstacleY and boxY < obstacleB:
            if boxR > obstacleX and boxX < obstacleR:
                return True

        return False

    def keyActions(self):
        key = pygame.key.get_pressed()

        player = self.player
        player.stopMovement()
        pressed = [i for i, j in enumerate(key) if j == 1]
        if constants.UPARROW in pressed:
            player.moveUp = True

        elif constants.DOWNARROW in pressed:
            player.moveDown = True

        if constants.LEFTARROW in pressed:
            player.moveLeft = True

        elif constants.RIGHTARROW in pressed:
            player.moveRight = True

    def moveAll(self):
        player = self.player
        moveX = 0
        moveY = 0

        if player.moveLeft:
            moveX -= player.SPEED

        if player.moveRight:
            moveX += player.SPEED

        if player.moveDown:
            moveY += player.SPEED

        if player.moveUp:
            moveY -= player.SPEED

        for wall in self.walls:
            wall.x -= moveX
            wall.y -= moveY

    def gameLoop(self):
        player = self.player

        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.keyActions()

                if event.type == pygame.KEYUP:
                    self.keyActions()

            # Movement logic
            self.moveAll()

            # Laser Collision
            playerBox = player.boxDims()


            # displays
            pygame.draw.rect(self.screen, constants.BLUE, playerBox)

            #Draw walls
            for wall in self.walls:
                pygame.draw.rect(self.screen, constants.RED, wall.boxDims())

            pygame.display.flip()
            self.screen.fill(constants.BLACK)

    def gameOver(self):
        endFont = pygame.font.SysFont('Impact', 90)
        gameOverMessage = "Game over"
        endMessage = endFont.render(gameOverMessage, False, constants.LIGHTBLUE)
        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.blit(endMessage, (200,300))

            pygame.display.flip()
            self.screen.fill(constants.BLACK)


if __name__ == '__main__':
    ropeGame = RopeGame()
    ropeGame.gameLoop()
    ropeGame.gameOver()
