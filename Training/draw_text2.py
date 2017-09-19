import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((1000, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    sysfont = pygame.font.SysFont(None, 72)
    message = sysfont.render("DORY 2nd STAGE", True, (0, 128, 128))
    message_rect = message.get_rect()
    theta = 0
    scale = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))
        theta += 5
        scale = (theta % 360) / 180
        tmp_msg = pygame.transform.rotozoom(message, theta, scale)
        tmp_rect = tmp_msg.get_rect()
        tmp_rect.center = (500, 150)

        SURFACE.blit(tmp_msg, tmp_rect)
        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()
