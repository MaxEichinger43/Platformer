import pygame
pygame.init()

'''
Variables
'''

scr_w = 1680
scr_h = 1050
scr_size = (scr_w, scr_h)
screen = pygame.display.set_mode(scr_size, 0, 0, 0, 1)
clock = pygame.time.Clock()
fps = 60
running = True
dt = 0
background = pygame.image.load("sprites/background.png")
gravity = 500
font = pygame.font.Font(None, 24)

# player
p_image = pygame.image.load("sprites/p1.png")
ground = 500 - p_image.get_height()
p_image_f = p_image
p_size = (p_image.get_width(), p_image.get_height())
p_pos = pygame.Vector2(500, ground)
p_velo = pygame.Vector2(400, 0)
p_rect = pygame.Rect(p_pos, p_size)
p_speed = p_velo.length()
p_speed_max = 500
p_facingR = True
p_facingL = False
p_jumping = False
p_falling = False
p_grounded = True
p_jump_height_max = 500
p_jump_height = 1
p_jump_force = 1000


'''
Objects
'''
class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display(self, y):
        debug_text = f"{self.name}: {self.value}"
        debug_surface = font.render(debug_text, True, (255, 0, 0))
        screen.blit(debug_surface, (10, y))


def checkPlayerPos():
    global p_grounded, p_falling
    if p_pos.y >= ground:
        p_grounded = True
    elif p_jumping:
        p_falling = False
    elif not p_jumping:
        p_falling = False


def movePlayer():
    global p_pos, p_rect, p_speed, p_image_f
    p_speed = p_velo.length()
    p_rect = pygame.Rect(p_pos, p_size)
    if p_facingL:
        p_image_f = pygame.transform.flip(p_image, 1, 0)
    else:
        p_image_f = p_image
    if p_pos.y <= ground - p_image.get_height():
        p_pos.y += gravity * dt


def drawPlayer(p_image_f):
    screen.blit(p_image_f, p_pos)


def controlPlayer(keys):
    global debug_mode, p_facingL, p_facingR, p_jumping, p_jump_height

    if keys[pygame.K_w]:
        pass

    if keys[pygame.K_a]:
        p_facingL = True
        p_facingR = False
        if p_speed < p_speed_max and p_facingL:
            p_pos.x -= p_velo.x * dt

    if keys[pygame.K_s]:
        pass

    if keys[pygame.K_d]:
        p_facingL = False
        p_facingR = True
        if p_speed < p_speed_max and p_facingR:
            p_pos.x += p_velo.x * dt

    if keys[pygame.K_SPACE]:
        if p_grounded and not p_jumping:
            p_jumping = True
            jump()
        if p_jumping:
            p_jump_height += 10 * dt
            jump()

    if keys[pygame.K_F1]:
        debug_mode = not debug_mode

def jump():
    if p_jump_height <= p_jump_height_max:
        p_pos.y -= 0.5 * abs(1 / p_jump_height**2 * p_jump_force) * dt



def debug():
    global p_pos, p_rect, p_speed, p_image_f, p_speed_max, p_facingR, p_facingL, dt
    variables = [
        Variable("p_pos", p_pos),
        Variable("p_rect", p_rect),
        Variable("p_speed", p_speed),
        Variable("p_image_f", p_image_f),
        Variable("p_speed_max", p_speed_max),
        Variable("p_facingR", p_facingR),
        Variable("p_facingL", p_facingL),
        Variable("dt", dt),
    ]

    y_position = 10
    for variable in variables:
        variable.display(y_position)
        y_position += 20


'''
Main Loop
'''

debug_mode = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            running = False
    screen.fill((130, 255, 255))
    screen.blit(background, (0,0))
    clock.get_time()
    keys = pygame.key.get_pressed()

    checkPlayerPos()
    controlPlayer(keys)

    movePlayer()

    drawPlayer(p_image_f)

    if debug_mode:
        debug()

    pygame.display.update()
    dt = clock.tick(fps) / 1000

pygame.quit()
