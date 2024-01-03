import pygame
import random
pygame.init()

scr_w = 1680
scr_h = 1050
scr_size = (scr_w, scr_h)
screen = pygame.display.set_mode(scr_size,0,0,0,1)
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("sprites/background.png")
gravity = 500
font = pygame.font.Font(None, 24)

# player
p_image = pygame.image.load("sprites/p1.png")
p_image_f = p_image
p_size = (p_image.get_width(), p_image.get_height())
p_pos = pygame.Vector2(500,400)
p_velo = pygame.Vector2(400,0)
p_acc = 600
p_decc = 800
p_rect = pygame.Rect(p_pos, p_size)
p_speed = p_velo.length()
p_speed_max = 500
p_facingR = True
p_facingL = False
p_on_ground = True
p_jump_height = 0
p_j_height_max = 200
p_jump_force = 1300
p_jumping = False

def movePlayer():
    global p_pos, p_rect, p_speed, p_image_f
    p_speed = p_velo.length()
    p_rect = pygame.Rect(p_pos, p_size)
    if p_facingL:
        p_image_f = pygame.transform.flip(p_image, 1, 0)
    else:
        p_image_f = p_image
    checkPlayerPosition()
    if not p_on_ground:
        p_pos.y += gravity * dt
    
def drawPlayer(p_image_f):
    screen.blit(p_image_f, p_pos)

def controlPlayer(keys):
    global debug_mode, p_facingL, p_facingR, p_jump_height, p_on_ground, p_jumping, p_pos

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
        checkPlayerPosition()
        if p_on_ground and not p_jumping:
            startJump()
        elif p_jumping and p_jump_height <= p_j_height_max and p_pos.y <= 500:
            jump()
        elif p_pos.y >= 500:
            endJump()
        
    if keys[pygame.K_F1]:
        debug_mode = not debug_mode


def checkPlayerPosition():
    global p_on_ground, p_jump_height
    if p_pos.y >= 500:
        p_on_ground = True
        p_jump_height = 0
    else:
        p_on_ground = False

def startJump():
    global p_jumping
    p_jumping = True

def endJump():
    global p_jumping, p_jump_height
    p_jumping = False
    p_jump_height = 0

def jump():
    global p_on_ground, p_pos, p_jump_force, p_jump_height
    if p_jump_force >= 0:
        p_pos.y += p_jump_force * dt
        p_jump_force -= gravity * dt
        p_jump_height += 1



def debug():
    global p_on_ground, p_jump_height, p_speed, p_speed_max, p_facingL, p_facingR, p_jumping, p_pos, p_velo, p_acc, gravity, dt
    fps = f"Fps: {clock.get_fps():.0f}"
    debug_surface = font.render(fps, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 10))
    loc = f"Loc: {p_pos.x:.0f}, {p_pos.y:.0f}"
    debug_surface = font.render(loc, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 30))
    velo = f"Velo: {p_velo.x:.0f}, {p_velo.y:.0f}"
    debug_surface = font.render(velo, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 50))
    acc = f"Acc: {p_acc:.0f}"
    debug_surface = font.render(acc, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 70))
    gravity_display = f"Gravity: {gravity}"
    debug_surface = font.render(gravity_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 90))
    dt_display = f"Delta Time: {dt:.6f}"
    debug_surface = font.render(dt_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 110))
    p_on_ground_display = f"On Ground: {p_on_ground}"
    debug_surface = font.render(p_on_ground_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 130))
    p_jump_height_display = f"Jump Height: {p_jump_height}"
    debug_surface = font.render(p_jump_height_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 150))
    p_speed_display = f"Player Speed: {p_speed}"
    debug_surface = font.render(p_speed_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 170))
    p_speed_max_display = f"Max Speed: {p_speed_max}"
    debug_surface = font.render(p_speed_max_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 190))
    p_facing_display = f"Facing Left: {p_facingL}, Facing Right: {p_facingR}"
    debug_surface = font.render(p_facing_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 210))
    p_jumping_display = f"Jumping: {p_jumping}"
    debug_surface = font.render(p_jumping_display, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 230))



debug_mode = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            running = False
    screen.fill((130,255,255))
    clock.get_time()
    keys = pygame.key.get_pressed()

    controlPlayer(keys)

    movePlayer()
    
    drawPlayer(p_image_f)


    if debug_mode:
        debug()

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()