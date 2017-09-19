import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    mousepos = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)

        for i, j in mousepos:
            pygame.draw.circle(SURFACE, (0, 255, 0), (i, j), 5)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
