import pygame
import random
from asteroid import Asteroid
import constants as C


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-C.ASTEROID_MAX_RADIUS, y * C.SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                C.SCREEN_WIDTH + C.ASTEROID_MAX_RADIUS, y * C.SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * C.SCREEN_WIDTH, -C.ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * C.SCREEN_WIDTH, C.SCREEN_HEIGHT + C.ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, size: int, position: pygame.Vector2, velocity: pygame.Vector2):
        asteroid = Asteroid(position.x, position.y, size)
        asteroid.velocity = velocity

    def update(self, dt: float):
        self.spawn_timer += dt
        if self.spawn_timer > C.ASTEROID_SPAWN_RATE:
            print("spawning asteroid")
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, C.ASTEROID_KINDS)
            self.spawn(kind, position, velocity)