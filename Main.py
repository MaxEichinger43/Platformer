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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gfx = pygame.image.load("sprites/p1.png")
        self.w = self.gfx.get_width()
        self.h = self.gfx.get_height()
        self.speed = 500
        self.body = pygame.Rect(self.x, self.y, self.w, self.h)
        self.is_jumping = False
        self.is_falling = True


    #def collisionDetection():

    def move(self):
        self.body.x = self.x
        self.body.y = self.y


    def grav(self):
        if self.is_falling:
            self.y += gravity * dt
        else:
            pass

    def draw(self):
        screen.blit(self.gfx, (self.x, self.y))

    def input(self):
        global debug_mode
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed * dt
        if keys[pygame.K_a]:
            self.x -= self.speed * dt
        if keys[pygame.K_s]:
            self.y += self.speed * dt
        if keys[pygame.K_d]:
            self.x += self.speed * dt

        if keys[pygame.K_SPACE]:
            p1.is_jumping = True

        if keys[pygame.K_F1]:
            debug_mode = not debug_mode


def debug():
    global p1_in_ground
    fps = f"Fps: {clock.get_fps():.0f}"
    debug_surface = font.render(fps, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 10))

    
p1 = Player(random.randrange(0, scr_w), 0)

debug_mode = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            running = False
    clock.get_time()
    screen.fill((130,255,255))
    p1.input()
    p1.move()
    p1.draw()

    if debug_mode:
        debug()

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()