


import pygame


def load_wizard():
    martial_jump = pygame.image.load("./assets/images/wizard2/WizardPack/Jump.png").convert_alpha()
    martial_attack = pygame.image.load("./assets/images/wizard2/WizardPack/Attack1.png").convert_alpha()
    martial_attack2 = pygame.image.load("./assets/images/wizard2/WizardPack/Attack2.png").convert_alpha()
    martial_run = pygame.image.load("./assets/images/wizard2/WizardPack/Run.png").convert_alpha()
    martial_death = pygame.image.load("./assets/images/wizard2/WizardPack/Death.png").convert_alpha()
    martial_hit = pygame.image.load("./assets/images/wizard2/WizardPack/TakeHit.png").convert_alpha()
    martial_idle = pygame.image.load("./assets/images/wizard2/WizardPack/Idle.png").convert_alpha()


    return [martial_idle,martial_run,martial_jump,martial_attack,martial_attack2,martial_hit,martial_death]