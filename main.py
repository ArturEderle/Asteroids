import sys

import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        pygame.event.pump()
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

if __name__=="__main__":
    main()
