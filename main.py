import pygame
from constants import *
from player import Player

def main():
    # load libs and mods from pygame
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable) # add containers statically to Player objects

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # is a circle with default radius PLAYER_RADIUS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updateable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000 #returns DeltaTime; runs every 1/60 of a second


if __name__ == "__main__":
    main()

