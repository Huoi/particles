import math
import pygame

PI = math.pi

class Particle:
    def __init__(self, pos, speed, angle, radius, colour=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.x = pos[0]
        self.y = pos[1]
        self.speed = speed
        self.angle = angle
        self.radius = radius
        self.colour = colour

    def update(self, surface):
        self.move()
        self.draw(surface)
        self.collide(surface)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius)

    def collide(self, surface):
        box = surface.get_rect()
        if self.x - self.radius < box.x: # Left
            self.angle = math.pi - self.angle
        if self.x + self.radius > box.x + box.width: # Right
            self.angle = math.pi - self.angle
        if self.y - self.radius < box.y: # Top
            self.angle = -self.angle
        if self.y + self.radius > box.y + box.height: # Bottom
            self.angle = -self.angle
