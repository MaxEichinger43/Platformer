import pygame
import random
pygame.init()

scr_w = 1680
scr_h = 1050
scr_size = (scr_w, scr_h)
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("sprites/background.png")
gravity = 200
font = pygame.font.Font(None, 24)

class Player:
    def __init__(self, x, y, gfx):
        self.x = x
        self.y = y
        self.gfx = gfx
        self.mask = pygame.mask.from_threshold(self.gfx, (0,0,0,255), )
        self.w = self.mask.get_size()[0]
        self.h = self.mask.get_size()[1]
        self.speed = 500
        self.body = self.mask.get_rect()
        self.is_jumping = False
        self.is_falling = True

    def move(self):
        self.body.x = self.x
        self.body.y = self.y

    def grav(self):
        self.y += gravity * (t_g ** 2) * dt

    def draw(self):
        screen.blit(self.gfx, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.body, 1, 1, 1)

def input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.y -= p1.speed * dt
    if keys[pygame.K_s]:
        p1.y += p1.speed * dt
    if keys[pygame.K_a]:
        p1.x -= p1.speed * dt
    if keys[pygame.K_d]:
        p1.x += p1.speed * dt

p1 = Player(random.randrange(0, scr_w), 0, pygame.image.load("sprites/p1.png"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.get_time()

    screen.blit(background, (0, 0))
    input()
    p1.move()
    p1.draw()

    dt = clock.tick(60) / 1000
    fps = f"Fps: {clock.get_fps():.0f}"
    debug_surface = font.render(fps, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 10))
    pygame.display.update()

pygame.quit()