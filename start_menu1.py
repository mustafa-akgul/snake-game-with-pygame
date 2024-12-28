import pygame, sys, random

screen_width = 600
screen_height = 600




def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.SysFont("arial", 25)
    clock = pygame.time.Clock()

    while True:
        screen.fill((149, 1, 252))
        text = font.render("Yılan Oyunu", True, (255, 255, 255))
        instruction = font.render("BAŞLA(space)", True, (255, 255, 255))
        instruction2 = font.render("ÇIK(q)", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 6))
        screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, screen_height // 2.2))
        screen.blit(instruction2, (screen_width // 2 - instruction.get_width() // 2, screen_height // 1.8))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    return

        pygame.display.flip()
        clock.tick(30)