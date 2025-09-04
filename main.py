import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    from asteroid import Asteroid
    Asteroid.containers = (asteroids, updatable, drawable)
    from shot import Shot
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for rock in asteroids.sprites():
            for bullet in shots.sprites():
                for bullet in shots.sprites():
                    if bullet.collides(rock):
                        bullet.kill()
                        rock.split()

        for rock in asteroids.sprites():
            if player.collides(rock):
                print("Game over!")
                return

        screen.fill((0, 0, 0))
        for sprite in drawable.sprites():
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
