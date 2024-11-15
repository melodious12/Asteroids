import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.add(self.containers)
        self.position = pygame.math.Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, SHOT_RADIUS*2, SHOT_RADIUS*2)
        self.velocity = pygame.math.Vector2(0, PLAYER_SHOOT_SPEED).rotate(self.direction)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = self.position