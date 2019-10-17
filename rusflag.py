import sys
import pygame

def run_game():
    pygame.init()
    sc = pygame.display.set_mode((400, 450))
    bg_color = (220, 220, 255)
    sc.fill(bg_color)
    # флэшток фигуры
    pygame.draw.rect(sc, (255, 155, 0), (52, 18, 10, 420))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

run_game()