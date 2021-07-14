import pygame

pygame.init()

tela_lagura = 800
tela_altura = int(tela_lagura * 0.8)

tela = pygame.display.set_mode((tela_lagura, tela_altura))
pygame.display.set_caption('WAR GAME')


class Soldado(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/jogador/jogador_img/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


jogador = Soldado(200, 200, 3)
jogador2 = Soldado(500, 200, 3)

run = True

while run:
    tela.blit(jogador.image, jogador.rect)
    tela.blit(jogador2.image, jogador2.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
