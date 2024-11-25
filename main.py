import pygame
from constants import *
from player import Player

def main():
    #initialization
    pygame.init()

    #create time relevant objects
    clock = pygame.time.Clock()
    dt = 0

    #create screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill screen with black
        screen.fill('black')

        #draw player on screen
        player.update(dt)
        player.draw(screen)
        


        #refresh screen
        pygame.display.flip()

        #tick clock set frame rate to 60fps
        dt = clock.tick(60)/1000






if __name__ == "__main__":
    main()