import sys, pygame
import math


class Colors:
    RED = (200, 70, 70)
    GREEN = (70, 200, 70)
    BLUE = (70, 70, 200)
    MID = (200, 70, 70)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.size = [1440, 400]
        self.screen = pygame.display.set_mode(self.size)

        self.circle_count = 0
        self.mid = 0
        self.centers = []

        self.radius = 30
        self.gap = self.radius * 3
        self.width = 5

        self.aradius = int(self.radius * 0.8)
        self.tortoise = 0
        self.t_pos = 0

        self.hare = 0
        self.h_pos = 0
        self.hare_speed = 2

    def create(self, circle_count, mid):
        self.circle_count = circle_count
        self.mid = mid - 1
        self.centers = []

    def draw_circle(self, pos, radius, color, width=0):
        pygame.draw.circle(self.screen, color, pos, radius, width)

    def draw_map(self, start, r, gap, w, left, right, odd=False, save=False):
        drawn = 0
        x, y = start

        if odd:
            drawn = 1
            self.draw_circle(start, r, Colors.BLUE, w)
            if save:
                self.centers.append(x)

        i = 0
        while drawn < self.circle_count:
            x1 = left - i * (2 * r + gap)
            self.draw_circle((x1, y), r, Colors.BLUE, w)
            x2 = right + i * (2 * r + gap)
            self.draw_circle((x2, y), r, Colors.BLUE, w)

            if save:
                self.centers.append(x1)
                self.centers.append(x2)

            drawn += 2
            i += 1

    def draw_arrows(self):
        y = self.size[1] // 2
        for pos in self.centers[:-1]:
            x = pos
            x += self.radius
            pygame.draw.line(self.screen, Colors.BLUE, (x, y), (x + self.gap, y), self.width // 2)

        x = self.centers[self.mid]
        length = self.centers[-1] - x
        sta = 0
        sto = math.pi

        rect = [x, y - 50, length, 200]
        pygame.draw.arc(self.screen, Colors.BLUE, rect, sto, sta, 5)

    def draw_hare_tort(self):
        x1 = self.tortoise[0]
        x2 = self.hare[0]

        if x1 == x2:
            self.draw_circle(self.tortoise, self.aradius, Colors.MID)
            return

        self.draw_circle(self.tortoise, self.aradius, Colors.GREEN)
        self.draw_circle(self.hare, self.aradius, Colors.WHITE)

    def travel(self):
        x, y = self.tortoise
        self.t_pos += 1
        self.h_pos += self.hare_speed

        if self.t_pos >= self.circle_count:
            self.t_pos = self.mid

        if self.h_pos == self.circle_count:
            self.h_pos = self.mid

        if self.h_pos == self.circle_count + 1:
            self.h_pos = self.mid + 1

        x = self.centers[self.t_pos]
        self.tortoise = [x, y]
        x = self.centers[self.h_pos]
        self.hare = [x, y]

    def gameLoop(self):
        tracker = 0
        x, y = self.size
        r = self.radius
        gap = self.gap
        w = self.width

        start = x // 2, y // 2
        odd = False

        x, y = start
        if self.circle_count % 2 == 0:
            left = x - (r + gap // 2)
            right = x + (r + gap // 2)

        else:
            odd = True
            left = x - r - gap - r
            right = x + r + gap + r

        self.draw_map(start, r, gap, w, left, right, odd, save=True)
        self.centers.sort()
        x = self.centers[0]
        self.tortoise = [x, y]
        x = self.centers[0]
        self.hare = [x, y]

        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_SPACE]:
                        self.travel()

                    if key[pygame.K_r]:
                        self.tortoise[0] = self.centers[0]
                        self.t_pos = 0

                    if key[pygame.K_h]:
                        self.hare[0] = self.centers[0]
                        self.h_pos = 0
                        self.hare_speed = 2

                    if key[pygame.K_t]:
                        self.tortoise[0] = self.centers[0]
                        self.t_pos = 0
                        self.hare[0] = self.centers[0]
                        self.h_pos = 0
                        self.hare_speed = 2

                    if key[pygame.K_s]:
                        self.hare_speed = 1

                    if key[pygame.K_f]:
                        self.hare_speed = 2
                        
                    if key[pygame.K_UP]:
                        return 2

                    if key[pygame.K_DOWN]:
                        return 3

                    if key[pygame.K_RIGHT]:
                        return 4

                    if key[pygame.K_LEFT]:
                        return 5

            self.draw_map(start, r, gap, w, left, right, odd)
            self.draw_arrows()
            self.draw_hare_tort()

            # self.screen.blit(self.textsurface, (0, 60))
            pygame.display.flip()
            self.screen.fill(Colors.BLACK)

    def gameMaster(self, circles, meet):
        br = 1  # True Run
        """
        1- normal
        2 - increase circles
        3 - decresase circles
        4 - decrease meet pos
        5 - increase meet pos
        """
        while br < 6:
            self.create(circles, meet)
            br = self.gameLoop()

            if br == 2:
                circles += 1
            elif br == 3:
                circles -= 1
            elif br == 4:
                meet += 1
            else:
                meet -= 1


if __name__ == '__main__':
    play = Game()
    l = 7
    s = 3
    play.gameMaster(l, s)
