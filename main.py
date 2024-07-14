import math, random
import pygame
from particle import Particle
from gui import Gui

WIDTH, HEIGHT = 1280, 720

def random_pos(radius):
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    return (x, y)

def random_angle():
    return random.uniform(-math.pi, math.pi)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

gui = Gui(10, 10, 10)

particles = []

def update_particles():
    if gui.count > len(particles):
        for _ in range(gui.count - len(particles)):
            particle = Particle(random_pos(gui.radius), gui.speed, random_angle(), gui.radius)
            particles.append(particle)
    else:
        for _ in range(len(particles) - gui.count):
            particles.pop(0)

    for particle in particles:
        particle.speed = gui.speed
        particle.radius = gui.radius

update_particles()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gui.updated:
        update_particles()
        gui.updated = False

    screen.fill((0, 0, 0))
    for particle in particles:
        particle.update(screen)

    pygame.display.flip()
    gui.update()
    dt = clock.tick(60) / 1000

gui.quit()
pygame.quit()
