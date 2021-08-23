import pygame
import os

pygame.init()
screen = pygame.display.set_mode([800, 533])
pygame.display.set_caption('War Game')
os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pygame.time.Clock()

menu = [0, 0]

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        mouse_pos = pygame.mouse.get_pos()
        mouse = mouse_pos[1]
        if mouse >= (400 / 2) < mouse <= ((400 / 2) + 21):
            menu[1] = 1
        elif mouse >= ((400 / 2) + 22) < mouse <= ((400 / 2) + 43):
            menu[1] = 2
        elif mouse < (400/ 2):
            menu[1] = 0
        elif mouse > ((400 / 2) + 43):
            menu[1] = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            menu[1] += 10

        if menu == [0, 0]:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (255, 255, 255))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) - 24, (400 / 2) + 22))
        elif menu == [0, 1]:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (0, 155, 255))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) - 24, (400 / 2) + 22))
        elif menu == [0, 2]:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (255, 255, 255))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            exit_game = font.render('Quit', True, (0, 155, 255))
            screen.blit(exit_game, ((800 / 2) - 24, (400 / 2) + 22))

        if menu == [0, 11]:
            menu = [1, 1]
        elif menu == [0, 12]:
            exit()

        if menu == [1, 0]:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            episode_1 = font.render('Episode 1', True, (255, 255, 255))
            screen.blit(episode_1, ((800 / 2) - 22, (400 / 2)))

            back = font.render('Quit', True, (255, 255, 255))
            screen.blit(back, ((800 / 2) - 24, (400 / 2) + 22))
        elif menu == [1, 1]:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            episode_1 = font.render('Episode 1', True, (0, 155, 255))
            screen.blit(episode_1, ((800 / 2) - 22, (400 / 2)))

            back = font.render('Quit', True, (255, 255, 255))
            screen.blit(back, ((800 / 2) - 24, (400 / 2) + 22))
        elif menu == [1, 2]:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            episode_1 = font.render('Episode 1', True, (255, 255, 255))
            screen.blit(episode_1, ((800 / 2) - 22, (400 / 2)))

            back = font.render('Quit', True, (0, 155, 255))
            screen.blit(back, ((800 / 2) - 24, (400 / 2) + 22))

        if menu == [1, 11]:
            menu = [1, 1]
        elif menu == [1, 12]:
            menu = [0, 2]

        pygame.display.update()
