


import pygame


def load_knight():
    knight_jump = pygame.image.load("./assets/images/knight/Sprites/Jump.png").convert_alpha()
    knight_attack = pygame.image.load("./assets/images/knight/Sprites/Attack.png").convert_alpha()
    knight_run = pygame.image.load("./assets/images/knight/Sprites/Run.png").convert_alpha()
    knight_death = pygame.image.load("./assets/images/knight/Sprites/Death.png").convert_alpha()
    knight_hit = pygame.image.load("./assets/images/knight/Sprites/TakeHit.png").convert_alpha()
    knight_idle = pygame.image.load("./assets/images/knight/Sprites/Idle.png").convert_alpha()


    return [knight_idle,knight_run,knight_jump,knight_attack,knight_attack,knight_hit,knight_death]