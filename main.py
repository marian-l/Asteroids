import pygame
from constants import *

def main():
    # print("Starting Asteroids!")
    # print("Screen width: " + str(constants.SCREEN_HEIGHT))
    # print("Screen height: " + str(constants.SCREEN_WIDTH))

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()

