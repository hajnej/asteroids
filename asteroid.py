import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen,"white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    split_asteroid_1_v = self.velocity.rotate(random_angle)
    split_asteroid_2_v = self.velocity.rotate(-random_angle)
    split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
    split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
    split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
    split_asteroid_1.velocity = split_asteroid_1_v * 1.2
    split_asteroid_2.velocity = split_asteroid_2_v * 1.2
