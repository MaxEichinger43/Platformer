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
gravity = 500
font = pygame.font.Font(None, 24)

def input():
    global debug_mode
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pass
    
    if keys[pygame.K_a]:
        pass
  
    if keys[pygame.K_s]:
        pass
 
    if keys[pygame.K_d]:
        pass

    if keys[pygame.K_SPACE]:
        pass
 

        if keys[pygame.K_F1]:
            debug_mode = not debug_mode


def debug():
    global p1_in_ground
    fps = f"Fps: {clock.get_fps():.0f}"
    debug_surface = font.render(fps, True, (255, 0, 0))
    screen.blit(debug_surface, (10, 10))


debug_mode = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            running = False
    clock.get_time()
    screen.fill((130,255,255))


    if debug_mode:
        debug()

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()