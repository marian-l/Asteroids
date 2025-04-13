from pygame import Vector2, draw, key, K_a, K_d, K_w, K_s, K_SPACE
import circleshape
import shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.timer = 0
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forwardVector = Vector2(0, 1).rotate(self.rotation)
        # forwardVector.rotate(self.rotation)
        self.position += forwardVector * PLAYER_SPEED * dt

    def shoot(self):
        s = shot.Shot(self.position.x, self.position.x)
        s.velocity = Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = key.get_pressed()

        self.timer = self.timer - dt

        if keys[K_a]:
            self.rotate(-dt)
        if keys[K_d]:
            self.rotate(dt)
        if keys[K_w]:
            self.move(dt)
        if keys[K_s]:
            self.move(-dt)
        if keys[K_SPACE]:
            if self.timer < 0:
                self.shoot()
                self.timer = 0.3

