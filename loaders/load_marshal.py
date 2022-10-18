

import pygame


def load_martial_arts():
    martial_jump = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/GoingUp.png").convert_alpha()
    martial_attack = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/Attack1.png").convert_alpha()
    martial_attack2 = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/Attack2.png").convert_alpha()
    martial_run = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/Run.png").convert_alpha()
    martial_death = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/Death.png").convert_alpha()
    martial_hit = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/TakeHit.png").convert_alpha()
    martial_idle = pygame.image.load("./assets/images/martial/MartialHero3/Sprites/Idle.png").convert_alpha()



    return [martial_idle,martial_run,martial_jump,martial_attack,martial_attack2,martial_hit,martial_death]