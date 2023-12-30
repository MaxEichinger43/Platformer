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


def movePlayer():
    global p_pos, p_rect, p_speed, p_image_f
    p_speed = p_velo.length()
    p_rect = pygame.Rect(p_pos, p_size)
    if p_facingL:
        p_image_f = pygame.transform.flip(p_image, 1, 0)
    else:
        p_image_f = p_image
    
def drawPlayer(p_image_f):
    screen.blit(p_image_f, p_pos)

def controlPlayer(keys):
    global debug_mode, p_facingL, p_facingR

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
        pass
 
        if keys[pygame.K_F1]:
            debug_mode = not debug_mode


def debug():
    global p1_in_ground
    fps = f"Fps: {clock.get_fps():.0f}"
    debug_surface = font.render(fps, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 10))
    loc = f"Loc: {p_pos.x:.0f}, {p_pos.y:.0f}"
    debug_surface = font.render(loc, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 30))
    velo = f"velo: {p_velo.x:.0f}, {p_velo.y:.0f}"
    debug_surface = font.render(velo, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 50))
    acc = f"acc: {p_acc:.0f}"
    debug_surface = font.render(acc, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 70))


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