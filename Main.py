import pygame
import random
pygame.init()

scr_w = 1680, scr_h = 1050 
scr_size = (scr_w, scr_h)
screen = pygame.display.set_mode(scr_size,0,0,0,1)
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("sprites/background.png")

class Player:
    def def __init__(self, x, y, gfx):
        self.x = x
        self.y = y
        self.gfx = gfx

        self.speed = 500
        self.jHeight = 100
    
    def move():
        self.x += self.speed * dt
    def draw():
        screen.blit(self.gfx, (self.x, self.y))

def input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.y -= 300 * dt
    if keys[pygame.K_s]:
        p1.y += 300 * dt
    if keys[pygame.K_a]:
        p1.x -= 300 * dt
    if keys[pygame.K_d]:
        p1.x += 300 * dt 

p1 = Player(random.randrange(0, scr_w), 0, pygame.image.load("sprites/p1.png"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    input()
    p1.move()
    p1.draw()

    pygame.display.update()
    dt = clock.tick(120) / 1000

pygame.quit()