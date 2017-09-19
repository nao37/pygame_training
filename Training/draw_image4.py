import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    logo = pygame.image.load("dory.jpg")
    theta = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((225, 225, 225))

        theta += 1

        # ロゴを回転し、中心が(200, 150)の位置にロゴを描写
        new_logo = pygame.transform.rotate(logo, theta)
        rect = new_logo.get_rect()
        rect.center = (200, 150)
        SURFACE.blit(new_logo, rect)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
