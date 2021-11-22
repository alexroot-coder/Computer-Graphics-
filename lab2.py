import pygame
import random


def fill_polygon(window,x1=0, y1=0, x2=0, y2=0):
     
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
    window.set_at((x, y),[255,255,255])    
    #window.set_at((x, y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    #pygame.draw.rect(window, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (x, y, 1, 1))
    arr = []
    
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
        window.set_at((x, y),[255,255,255])
        #window.set_at((x, y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #pygame.draw.rect(window, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (x, y, 1, 1))
        arr.append((x,y))
    return arr


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
    
    #pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
    window.set_at((x, y),[255,0,0])
    arr = []
    
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
        window.set_at((x, y),[255,0,0])
        #pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
        arr.append((x,y))
    return arr



def scan_line_set(x1=0, y1=0, x2=0, y2=0):
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
    
    #pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
    arr = []
    
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
        #pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
        arr.append((x,y))
    return arr

pygame.init()
#a = [(39, 348), (68, 300), (277, 148),(350, 298), (231, 314), (531, 514) ]
window = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()
       #x1  y1     x2  y2     x3    y3
a = [(150,250), (70, 300),(10,700), (350, 400),(700, 100)]
b = [(350,650), (370, 600),(110,750), (360, 450)] 


x,y = 150,270

start_pos = x,y

#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 30)
#textsurface = myfont.render(str(N), False, (255, 255, 255))

black = [255, 255, 255]

yellow = [255, 255, 0]
x1 = 100
y1 = 200
x2 = 800
y2 = 800

aa = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)
    lines = []
    tmp = -1
    for i in range(0,len(a)):
        lines.append(draw_line(window,a[i][0],a[i][1],a[tmp][0],a[tmp][1]))
        tmp = i
      
    scan_line = draw_line(window,x1,y1,x2,y2)
    
    for line in lines:
        for h,k in line:
            for h1,k1 in scan_line:
                if (h,k) == (h1,k1):
                    aa.append((h,k))

    for i in range(len(aa)):
       fill_polygon(window,aa[0][0],aa[0][1],aa[-1][0],aa[-1][1])

    #window.blit(textsurface,(0,0))
    #pygame.draw.polygon(window,black,[(39, 348), (68, 300), (277, 148),(350, 298), (231, 314), (531, 514)],True)    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
exit()