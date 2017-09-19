import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        # 白：横線
        for i in range(0, 300, 25):
            pygame.draw.line(SURFACE, (255, 255, 255), (0, i), (400, i))

        # 白：縦線
        for i in range(0, 400, 25):
            pygame.draw.line(SURFACE, (255, 255, 255), (i, 0), (i, 300))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()

