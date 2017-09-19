import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    mousepos = []
    mousedown = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True

            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)

            elif event.type == MOUSEBUTTONUP:
                mousedown = False

        SURFACE.fill((225, 225, 225))
        if len(mousepos) > 1:
            pygame.draw.aalines(SURFACE, (0, 225, 0), False, mousepos)

        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()




# import sys
# import pygame
# from pygame.locals import QUIT, \
#     MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP

# pygame.init()
# SURFACE = pygame.display.set_mode((400, 300))
# FPSCLOCK = pygame.time.Clock()

# def main():
#     """ main routine """
#     mousepos = []
#     mousedown = False

#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()

#             elif event.type == MOUSEBUTTONDOWN:
#                 mousedown = True

#             elif event.type == MOUSEMOTION:
#                 if mousedown:
#                     mousepos.append(event.pos)

#             elif event.type == MOUSEBUTTONUP:
#                 mousedown = False
#                 mousepos.clear()

#         SURFACE.fill((255, 255, 255))
#         if len(mousepos) > 1:
#             pygame.draw.lines(SURFACE, (255, 0, 0), False, mousepos)

#         pygame.display.update()
#         FPSCLOCK.tick(50)

# if __name__ == '__main__':
#     main()


# import sys
# import pygame
# import random
# from pygame.locals import QUIT

# pygame.init()
# SURFACE = pygame.display.set_mode((400, 300))
# FPSCLOCK = pygame.time.Clock()


# def main():
#   """ main routine """
#   logo = pygame.image.load("dory.jpg")
#   theta = 0

#   while True:
#       for event in pygame.event.get():
#           if event.type == QUIT:
#               pygame.quit()
#               sys.exit()

#       SURFACE.fill((225, 225, 225))
#       num = random.randint(10,100)
#       aaa = random.randint(100, 300)
#       bbb = random.randint(100, 300)

#       theta += 1

#       # ロゴを回転し、中心が(200, 150)の位置にロゴを描写
#       new_logo = pygame.transform.rotate(logo, theta)
#       rect = new_logo.get_rect()
#       rect.center = (aaa, bbb)
#       SURFACE.blit(new_logo, rect)

#       pygame.display.update()
#       FPSCLOCK.tick(num)

# if __name__ == '__main__':
#   main()
