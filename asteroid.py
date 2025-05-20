import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, size: int):
        radius =  ASTEROID_MIN_RADIUS * size
        self.kind: int = size
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        if self.kind > 1:
            angle = random.uniform(20, 50)
            asteroid = Asteroid(*self.position, self.kind - 1)
            asteroid.velocity = self.velocity.rotate(angle) * 1.2
            asteroid = Asteroid(*self.position, self.kind - 1)
            asteroid.velocity = self.velocity.rotate(-angle) * 1.2
        self.kill()
