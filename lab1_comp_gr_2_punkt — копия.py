import pygame
import math
import random

def draw_line(window,x1=0, y1=0, x2=0, y2=0):
     
    dx = x2 - x1
    dy = y2 - y1
    
    sign_x = 1 if dx>0 else -1 if dx<0 else 0
    sign_y = 1 if dy>0 else -1 if dy<0 else 0
    
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    
    x, y = x1, y1
    
    error, t = el/2, 0        
    
    pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
    
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
        
            
def points(radius,angle):
    x = radius * math.cos(angle * math.pi / 180)
    y = radius * math.sin(angle * math.pi / 180)
    return x,y

N = int(input())

angle1 = 360/N
print(angle1)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render(str(N), False, (255, 255, 255))
window = pygame.display.set_mode((300, 300))

coords = []

for i in range(0,360,int(angle1)):
    coords.append(points(random.randint(0,150),i))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)
    
    window.blit(textsurface,(0,0))

    # for i in range(0,360,int(angle1)):
    #     coord = points(random.randint(0,50),i)
    #     draw_line(window,150,150,coord[0]+150,coord[1]+150)
    for coord in coords:
        draw_line(window,150,150,coord[0]+150,coord[1]+150)
        
    pygame.display.flip()
pygame.quit()
exit()