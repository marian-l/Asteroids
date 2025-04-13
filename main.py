import pygame
from constants import *
from player import Player

def main():
    # print("Starting Asteroids!")
    # print("Screen width: " + str(constants.SCREEN_HEIGHT))
    # print("Screen height: " + str(constants.SCREEN_WIDTH))

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # is a circle with default radius PLAYER_RADIUS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000 #returns DeltaTime; runs every 1/60 of a second


if __name__ == "__main__":
    main()

