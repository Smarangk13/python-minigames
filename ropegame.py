import sys, pygame
import random


class Laser:
    x = 0
    y = 0
    width = 0
    height = 0

    def setLaser(self):
        self.width = random.randint(300, 600)
        self.height = 10

        #left or right side spawn
        randNum = random.randint(0, 1)
        if randNum == 0:
            self.x = 0
        else:
            self.x = RopeGame.constants.WINDOWWIDTH - self.width

        self.y = 200

class greenBox:
    x = 0
    y = 0
    width = 0
    height = 0

    def setObjective(self):
        self.width = random.randint(20, 20)
        self.height = 10

        self.x = random.randint(0, 900)
        self.y = 200

class Player:
    WIDTH = 40
    HEIGHT = 80
    SPEED = 5
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def stopMovement(self):
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False


class Rope:
    x = 200
    y = 0
    WIDTH = 10
    height = 50


class RopeGame:
    class constants:
        WINDOWWIDTH = 900
        WINDOWHEIGHT = 700
        BLACK = (0, 0, 0)
        RED = (250, 0, 0)
        BLUE = (0, 0, 200)
        BROWN = (66, 22, 14)
        GREEN = (0,128,0)
        LASERSPEED = 10
        LASERS = 4
        OBJECTIVES = 2
        LASERSTART = 200

        LEFTARROW = 276
        UPARROW = 273
        RIGHTARROW = 275
        DOWNARROW = 274

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        size = [self.constants.WINDOWWIDTH, self.constants.WINDOWHEIGHT]
        self.screen = pygame.display.set_mode(size)

        self.player = Player(200, 40)
        self.rope = Rope()
        self.laserArray = []
        self.objectiveArray =[]

        self.gameSetup()

    def gameSetup(self):
        laser_offset = self.constants.WINDOWHEIGHT / self.constants.LASERS
        laser_pos = self.constants.LASERSTART

        for i in range(self.constants.LASERS):
            laser = Laser()
            laser.setLaser()
            laser.y = laser_pos
            laser_pos += laser_offset

            self.laserArray.append(laser)

    @staticmethod
    def testCollision(box1, box2):
        box1X = box1[0]
        box1Y = box1[1]
        box1W = box1[2]
        box1H = box1[3]

        box2X = box2[0]
        box2Y = box2[1]
        box2W = box2[2]
        box2H = box2[3]

        if box1Y < box2Y + box2H and box1Y + box1H > box2Y:
            if box2X < box1X + box1W and box2X + box2W > box1X:
                return True

        return False

    def keyActions(self):
        key = pygame.key.get_pressed()

        player = self.player
        player.stopMovement()
        pressed = [i for i, j in enumerate(key) if j == 1]

        # key = (0,0,0,1,0,1)
        # key.index(1) = 3
        # pressed [3,5]
        #  for i, j in enumerate(key):
        #   # i 0 1 2 3
        #   # j 0 0 0 1 0 1
        #   # for i in range(len(key))
        #   # j = key[i]
        #   # if j==1
        #   # pressed.append(i)
        #   pass

        if self.constants.UPARROW in pressed:
            player.moveUp = True

        elif self.constants.DOWNARROW in pressed:
            player.moveDown = True

        if self.constants.LEFTARROW in pressed:
            player.moveLeft = True

        elif self.constants.RIGHTARROW in pressed:
            player.moveRight = True

    def gameLoop(self):
        rope = self.rope
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
            if player.moveLeft:
                player.x -= player.SPEED

            if player.moveRight:
                player.x += player.SPEED

            if player.moveDown:
                player.y += player.SPEED

            if player.moveUp:
                player.y -= player.SPEED

            # Laser Collision
            playerBox = [player.x, player.y, player.WIDTH, player.HEIGHT]

            for laserNo, laser in enumerate(self.laserArray):
                laserBox = [laser.x, laser.y, laser.width, laser.height]
                pygame.draw.rect(self.screen, self.constants.RED, laserBox)

                if self.testCollision(laserBox, playerBox):
                    print("in laser", laserNo)

                laser.y -= self.constants.LASERSPEED
                if laser.y < 0:
                    laser.setLaser()
                    laser.y = self.constants.WINDOWHEIGHT

            print(self.objectiveArray)
            #objective collecting
            for objectiveNo, greenBox in enumerate(self.objectiveArray):
                greenBox = [greenBox.x, greenBox.y, greenBox.WIDTH, greenBox.HEIGHT]
                pygame.draw.rect(self.screen, self.constants.GREEN, greenBox)
                print(greenBox)
                if self.testCollision(greenBox, playerBox):
                    print("Check point!")

            # Rope Positioning
            rope.height = player.y
            rope.x = int((player.x + (player.x + player.WIDTH)) / 2)
            ropeBox = [rope.x, rope.y, rope.WIDTH, rope.height]

            # displays
            pygame.draw.rect(self.screen, self.constants.BLUE, playerBox)
            pygame.draw.rect(self.screen, self.constants.BROWN, ropeBox)

            pygame.display.flip()
            self.screen.fill(self.constants.BLACK)


if __name__ == '__main__':
    ropeGame = RopeGame()
    ropeGame.gameLoop()
