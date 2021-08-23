import pygame

pygame.init()
screen = pygame.display.set_mode([800, 533])
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()

bg = pygame.sprite.Sprite(player_group)
bg.image = pygame.image.load('../../utilitie/images/background/campo.png')
bg.image = pygame.transform.scale(bg.image, [800, 533])
bg.rect = bg.image.get_rect()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player_group.draw(screen)
    player_group.update()
    pygame.display.update()
