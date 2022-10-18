


import pygame


def load_knight():
    knight_attack = pygame.image.load("./assets/images/knight/Sprites/Attack.png").convert_alpha()
    knight_run = [pygame.image.load("./assets/images/knight/Sprites/Dash.png").convert_alpha(),8]