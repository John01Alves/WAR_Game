import pygame

# screen = pygame.display.set_mode([800, 533])


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/pleyer/running/0.png')
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = self.image.get_rect()
        self.rect.center = (400, 385)
        self.speed = 0
        self.reverse = False

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 8
            self.reverse = False
        if keys[pygame.K_RIGHT]:
            self.rect.x += 8
            self.reverse = True
        else:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0
        elif self.rect.right > 800:
            self.rect.right = 800
            self.speed = 0

    # def rev(self):
        # self.screen.blit(pygame.transform.flip(self.image, self.reverse, False), self.rect)
