import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # load libs and mods from pygame
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # add containers statically to Player objects
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # is a circle with default radius PLAYER_RADIUS
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game over!")
                return

            for shot in shots:
                if asteroid.checkCollision(shot):
                    shot.kill()
                    asteroid.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000 #returns DeltaTime; runs every 1/60 of a second


if __name__ == "__main__":
    main()

