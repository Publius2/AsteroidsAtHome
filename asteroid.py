import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        return pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        random_angel = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(random_angel)
        asteroid2_velocity = self.velocity.rotate(-random_angel)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) 
        asteroid1.velocity = asteroid1_velocity * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = asteroid2_velocity * 1.2

