import pygame
import sys
from random import uniform as func

pygame.init()

WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")

white = (255, 255, 255)
black = (0, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
radius = 10

velocity = 8
vx = velocity * func(-1, 1)
vy = velocity * func(-1, 1)

border_l = radius
border_r = WIDTH - radius
border_u = radius
border_d = HEIGHT  

platform_height = 10
platform_width = 80
xp = (WIDTH - platform_width) // 2
yp = HEIGHT - platform_height
vp = 10

score = 0
num = 1.5 

font = pygame.font.SysFont(None, 36)

def drawWindow():
    win.fill(black)

    pygame.draw.line(win, white, (border_l, 0), (border_l, HEIGHT))  
    pygame.draw.line(win, white, (border_r, 0), (border_r, HEIGHT))  
    pygame.draw.line(win, white, (0, border_u), (WIDTH, border_u))    

    pygame.draw.circle(win, white, (int(x), int(y)), radius)

    pygame.draw.rect(win, white, (xp, yp, platform_width, platform_height))

    pygame.display.update()

def drawScore(score):
    win.fill(black)
    text = font.render(f"Your score: {score}", True, white)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > border_l:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp + platform_width < border_r:
        xp += vp

    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy

    if y + vy > border_d:
        if xp <= x + vx <= xp + platform_width and y + radius <= yp:
            vy = -vy
        
            vx *= num
            vy *= num
            score += 1
        else:
            drawScore(score)
            break

    x += vx
    y += vy

    drawWindow()

pygame.quit()
sys.exit()
