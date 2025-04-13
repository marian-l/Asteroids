from pygame import draw
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        draw.circle(screen, "white", self.position, constants.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt