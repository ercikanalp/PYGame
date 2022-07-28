import pygame

pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption('Game Screen')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

main_surface = pygame.image.load('images/background.jpg').convert_alpha()
text_surface = test_font.render('Text', False, 'Black')
head = pygame.image.load('images/kelle.png').convert_alpha()
dollar = pygame.image.load('images/dollar.png').convert_alpha()
head_x_pos = 600

while True:
    for event in (pygame.event.get()):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(main_surface, (0, 0))
    screen.blit(text_surface,(680,50))
    head_x_pos -= 3
    if head_x_pos < -100:
        head_x_pos = 800
    screen.blit(head, (head_x_pos, 270))
    screen.blit(dollar, (100,270))
    pygame.display.update()
    clock.tick(60)