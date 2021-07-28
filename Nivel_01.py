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
    def __init__(self, jogador_tipo, x, y, scale, veloc):
        pygame.sprite.Sprite.__init__(self)
        self.jogador_tipo = jogador_tipo
        self.veloc = veloc
        self.direcao = 1
        self.virar = False
        self.lista_animacao = []
        self.index = 0
        self.atualizar_tempo = pygame.time.get_ticks()

        for i in range(5):
            img = pygame.image.load(f'img/{self.jogador_tipo}/jogador_img/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
            self.lista_animacao.append(img)
            self.image = self.lista_animacao[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def atualizar_animacao(self):
        animacao_fresh = 90
        self.image = self.lista_animacao[self.index]
        if pygame.time.get_ticks() - self.atualizar_tempo > animacao_fresh:
            self.atualizar_tempo = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.lista_animacao):
            self.index = 0

    def movimento(self, movimento_esquerda, movimento_direita):
        dx = 0
        dy = 0
        if movimento_esquerda:
            dx = - self.veloc
            self.virar = True
            self.direcao = -1
        if movimento_direita:
            dy = self.veloc
            self.virar = False
            self.direcao = 1
        self.rect.x += dx
        self.rect.x += dy

    def desenho(self):
        tela.blit(pygame.transform.flip(self.image, self.virar, False), self.rect)


jogador = Soldado('jogador', 200, 200, 2, 5)
inimigo = Soldado('inimigo', 400, 200, 2, 5)

run = True

while run:
    relogio.tick(FPS)
    desenho_bg()
    jogador.atualizar_animacao()
    inimigo.atualizar_animacao()
    jogador.desenho()
    inimigo.desenho()
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
