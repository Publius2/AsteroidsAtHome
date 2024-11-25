import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #initialization
    pygame.init()

    #create time relevant objects
    clock = pygame.time.Clock()
    dt = 0

    #create screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    
    #create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #create asteroid field
    asteroidfield = AsteroidField()

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill screen with black
        screen.fill('black')

        for member in updateable: member.update(dt)
        for member in drawable: member.draw(screen)
        for member in asteroids: 
            if member.is_colliding(player):
                print("Game over!")
                return
            for shot in shots:
                if member.is_colliding(shot):
                    shot.kill()
                    member.split()
        


        #refresh screen
        pygame.display.flip()

        #tick clock set frame rate to 60fps
        dt = clock.tick(60)/1000






if __name__ == "__main__":
    main()