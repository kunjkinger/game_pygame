import pygame,sys
import random
pygame.init()

screen = pygame.display.set_mode((1280,720)) #width,height
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1_bg = pygame.image.load('Cloud1.png')
cloud2_bg = pygame.image.load('Cloud2.png')
crosshair =  pygame.image.load('crosshair.png')
duck_surface = pygame.image.load('duck.png')

land_position_y = 560
land_speed = 1

water_position_y = 640
water_speed = 1.5

game_font = pygame.font.Font(None, 60)
text_surface = game_font.render('You Won!',True,(255,255,255))
text_rect = text_surface.get_rect(center=(640,360))
ducklist = []
for duck in range(20):
    duck_position_x = random.randrange(50,1200)
    duck_position_y = random.randrange(120,600)
    duck_rect = duck_surface.get_rect(center=(duck_position_x, duck_position_y))
    ducklist.append(duck_rect)

while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(ducklist):
                if duck_rect.collidepoint(event.pos):
                #if crosshair_rect.colliderect(duck_rect):
                    del ducklist[index]
        
    
    
    screen.blit(wood_bg,(0,0)) # 0,0 is the top left position
    land_position_y -= land_speed
    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1
    
    for duck_rect in ducklist:
        screen.blit(duck_surface,duck_rect)
        
    if len(ducklist) <= 0:
        screen.blit(text_surface,text_rect)
        
    screen.blit(land_bg,(0,land_position_y))
    
    
    water_position_y += water_speed
    if water_position_y <= 620 or water_position_y >= 680:
        water_speed *= -1
    
    screen.blit(water_bg,(0,water_position_y))
    

    screen.blit(crosshair,crosshair_rect)
    screen.blit(cloud1_bg,(15,25))
    screen.blit(cloud2_bg,(50,25))
    
    
    pygame.display.update()
    clock.tick(120)