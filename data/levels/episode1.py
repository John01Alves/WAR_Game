import pygame
from data.players.player import Player


def level_one():
    pygame.init()
    screen = pygame.display.set_mode([800, 533])
    clock = pygame.time.Clock()

    player_group = pygame.sprite.Group()

    bg = pygame.sprite.Sprite(player_group)
    bg.image = pygame.image.load('utilitie/images/background/campo.png')
    bg.image = pygame.transform.scale(bg.image, [800, 533])
    bg.rect = bg.image.get_rect()

    player = Player(player_group)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        player_group.draw(screen)
        player.update()
        pygame.display.update()
