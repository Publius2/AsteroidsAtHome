import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, GAME_FONT, score):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
