
import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from logger import log_event
from constants import ASTEROID_MIN_RADIUS



class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        first_velocity = self.velocity.rotate(random_angle)
        second_velocity = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(
            self.position.x,
            self.position.y,
            new_radius
        )

        second_asteroid = Asteroid(
            self.position.x,
            self.position.y,
            new_radius
        )

        first_asteroid.velocity = first_velocity * 1.2
        second_asteroid.velocity = second_velocity * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
