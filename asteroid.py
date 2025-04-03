import pygame.draw
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            random_vector1 = self.velocity.rotate(random_angle)
            random_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            smaller_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            smaller_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            smaller_ast1.velocity = random_vector1 * 1.2
            smaller_ast2.velocity = random_vector2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)