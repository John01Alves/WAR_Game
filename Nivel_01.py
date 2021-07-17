import pygame

pygame.init()

tela_lagura = 800
tela_altura = int(tela_lagura * 0.8)

tela = pygame.display.set_mode((tela_lagura, tela_altura))
pygame.display.set_caption('WAR GAME')

relogio = pygame.time.Clock()
FPS = 60

movimento_esquerda = False
movimento_direita = False

BG = (233, 212, 96, 1)

def desenho_bg():
    tela.fill(BG)


class Soldado(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, veloc):
        pygame.sprite.Sprite.__init__(self)
        self.veloc = veloc
        img = pygame.image.load('img/jogador/jogador_img/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def movimento(self, movimento_esquerda, movimento_direita):
        dx = 0
        dy = 0
        if movimento_esquerda:
            dx = - self.veloc
        if movimento_direita:
            dy = self.veloc
        self.rect.x += dx
        self.rect.x += dy

    def desenho(self):
        tela.blit(self.image, self.rect)


jogador = Soldado(200, 200, 3, 5)

run = True

while run:
    relogio.tick(FPS)
    desenho_bg()
    jogador.desenho()
    jogador.movimento(movimento_esquerda, movimento_direita)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movimento_esquerda = True
            if event.key == pygame.K_d:
                movimento_direita = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movimento_esquerda = False
            if event.key == pygame.K_d:
                movimento_direita = False
    pygame.display.update()
pygame.quit()
