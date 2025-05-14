from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

import sys
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # init clock
    c = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # spawn player
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # spawn asteroid field
    af = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen black
        screen.fill((0, 0, 0))

        # update updatables group
        updatable.update(dt)

        # check for collisions
        for a in asteroids:
            if p.collides_with(a):
                sys.exit("Game over!")

        for a in asteroids:
            for bullet in shots:
                if bullet.collides_with(a):
                    a.split()
                    bullet.kill()

        # draw drawables group
        for d in drawable:
            d.draw(screen)
        # refresh the screen
        pygame.display.flip()

        dt = (c.tick(60)/1000)


if __name__ == "__main__":
    main()