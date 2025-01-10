import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    field = AsteroidField()
    player = Player(player_x, player_y)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                game_over = True
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

