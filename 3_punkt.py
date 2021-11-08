import pygame

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
    
    #window.blit(textsurface,(0,0))
    pygame.draw.polygon(window,black,[(39, 348), (68, 300), (277, 148),(350, 298), (231, 314), (531, 514)],True)    
    pygame.display.flip()
pygame.quit()
exit()


