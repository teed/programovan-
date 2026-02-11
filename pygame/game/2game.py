import pygame


pygame.init()
Icon = pygame.image.load("icon.png.webp")


pygame.display.set_icon(Icon)

screen =pygame.display.set_mode((400, 500))
color1="red"
color = (255,255,0)

running = True


while running:
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    screen .fill(color1)
    screen .blit(Icon, (70,30))
    
    pygame.draw.rect(screen, color,
                     pygame.Rect (30, 30, 60, 60))
    pygame.display.flip()    