import pygame



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
        pygame.draw.rect(window, (255, 255, 0), (x, y, 1, 1))
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
a = [(150,250), (70, 300), (350, 400),(100,700),(700, 100)] 


x,y = 150,270

start_pos = x,y

#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 30)
#textsurface = myfont.render(str(N), False, (255, 255, 255))

black = [255, 255, 255]

yellow = [255, 255, 0]
x1 = 0
y1 = 100
x2 = 800
y2 = 100

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)
    lines = []
    tmp = -1
    for i in range(0,len(a)):
        asd = draw_line(window,a[i][0],a[i][1],a[tmp][0],a[tmp][1])
        lines.append(asd)
        tmp = i
    # tmp = -1

    scan_line = scan_line_set(x1,y1,x2,y2)

    if(y1 > 700):
        y1 = 100

    if(y2 > 700):
        y2 = 100

    y1+=1
    y2+=1

    dots_connection_with_scanline = []

    for line in lines:
        for h,k in line:
            for h1,k1 in scan_line:
                if (h,k) == (h1,k1):
                    #print(line)

                    #if(line[0],line[-1] != line[0],line[-1]):
                    #draw_line(window,h,k,h1,k1)
                    dots_connection_with_scanline.append((h,k,line[0],line[-1]))
                    #window.set_at((h,k),[255,0,0])



    dots_connection_with_scanline.sort()
    #for dot in dots_connection_with_scanline:
        
    #if(len(dots_connection_with_scanline) != 0):
        #draw_line(window,dots_connection_with_scanline[20][0],dots_connection_with_scanline[20][1],dots_connection_with_scanline[21][0],dots_connection_with_scanline[21][1])



    #window.blit(textsurface,(0,0))
    #pygame.draw.polygon(window,black,[(39, 348), (68, 300), (277, 148),(350, 298), (231, 314), (531, 514)],True)    
    pygame.display.flip()
pygame.quit()
exit()