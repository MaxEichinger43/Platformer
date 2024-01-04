import platform
import random
import pygame

'''
Variables
'''
screen_w = 1680
screen_h = 1050
screen_size = (screen_w, screen_h)
screen = pygame.display.set_mode(screen_size, 0, 0, 0, 1)
clock = pygame.time.Clock()
fps = 60
running = True
dt = 0

# variables
img = pygame.image.load("sprites/p1.png")
imgl = pygame.transform.flip(img, 1, 0)
imgfinal = img
ground = 400
x = 525
y = ground - 400
v = 400
gravity = 9810
falling = False
grounded = True
jumping = False
jt = 0
ft = 0
jmax = 2000
jmin = 500
jump_force = jmax
jump_height = jmin

'''
Objects
'''
class Platform:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
    def spawn(self):
        self.rect = pygame.Rect(self.pos, self.size)
    def update(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        pygame.draw.rect(screen, (20, 200, 100), self.rect)
        self.pos[0] -= 100 * dt
        

def check():
    global x, y, falling, imgl, img, imgfinal, grounded, ft, jt
    if y >= ground:
        grounded = True
        falling = False
        ft = 0
        jt = 0
    elif not jumping:
        falling = True
        grounded = False


def handleInput(keys):
    global x, y, imgfinal, jumping
    if keys[pygame.K_SPACE] and grounded:  # Jump only when grounded
        startJump()
    if keys[pygame.K_a]:
        imgfinal = imgl
        x -= v * dt
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_d]:
        imgfinal = img
        x += v * dt

def update():
    global x, y, imgfinal, ft, jumping
    if falling:
        y += gravity * dt * ft**2
        ft += 1 * dt
    elif jumping:
        jump()
    screen.blit(imgfinal, (x, y))
    if y >= ground:
        y = ground

def startJump():
    global grounded, jumping, falling
    grounded = False
    jumping = True
    falling = False

def jump():
    global y, ft, jt, falling, jumping, jump_force, keys, jump_height
    if jump_force <= 0 or jump_height >= jmax:
        endJump()
    else:
        y -= jump_force * dt
        jump_force -= gravity * dt
    if jump_height <= jmax and keys[pygame.K_SPACE]:
        jump_height += jmax * dt

def endJump():
    global jumping, falling, jump_force, jump_height
    jumping = False
    falling = True
    jump_force = jmax
    jump_height = jmin


platform1 = Platform([1700, ground - random.random() * 300], (800, 100))
platform1.spawn()
platform2 = Platform([1700, ground - random.random() * 300], (800, 100))
platform2.spawn()

'''
Main loop
'''
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            running = False
    screen.fill((130, 255, 255))
    clock.get_time()
    keys = pygame.key.get_pressed()
    platform1.update()
    platform2.update()

    check()
    handleInput(keys)
    update()

    pygame.display.flip()
    dt = clock.tick(fps) / 1000

pygame.quit()
