import pygame

from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.__rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, delta_time: float|int ) -> None:
        self.__rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time: float|int) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)

    def move(self, delta_time: float|int ) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.__rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector