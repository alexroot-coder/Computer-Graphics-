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

a = [(39, 348), (68, 300), (277, 148),(350, 298), (231, 314), (531, 514) ]

pygame.init()
#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 30)
#textsurface = myfont.render(str(N), False, (255, 255, 255))
window = pygame.display.set_mode((800, 800))
black = [255, 255, 255]
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)
    tmp = -1
    for i in range(0,len(a)):
        draw_line(window,a[i][0],a[i][1],a[tmp][0],a[tmp][1])
        tmp = i
    
    #window.blit(textsurface,(0,0))
    #pygame.draw.polygon(window,black,[(39, 348), (68, 300), (277, 148),(350, 298), (231, 314), (531, 514)],True)    
    pygame.display.flip()
pygame.quit()
exit()
