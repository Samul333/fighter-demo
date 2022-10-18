import secrets
import pygame
from fighter import Fighter
from pygame import mixer

from loaders.load_knight import load_knight


pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


#define colors
RED = (255,0,0)
YELLOW = (66, 141, 245)
WHITE=(255,255,255)


def main_game():
        
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    load_knight()
    pygame.display.set_caption("Brawllar")

    bg_image = pygame.image.load("assets/images/background/bg4.jpg").convert_alpha()
    warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
    wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()
    sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
    magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
    running = pygame.mixer.Sound("assets/audio/running.mp3")
    
    you_win = pygame.mixer.Sound("assets/audio/you-win.mp3")

    pygame.mixer.music.load("assets/audio/music.mp3")
    # pygame.mixer.music.play(-1,0.0,5000)
    WARRIOR_ANIMATION_STEPS = [10,8,1,7,7,3,7]
    WIZARD_ANIMATION_SETPS = [8,8,1,8,8,3,7]

    WARRIOR_SIZE = 162
    WARRIOR_SCALE = 4
    WARRIOR_OFFSET= [72,56]
    WARRIOR_DATA = [WARRIOR_SIZE,WARRIOR_SCALE,WARRIOR_OFFSET]
    WIZARD_SIZE = 250   
    WIZARD_SCALE = 3
    WIZARD_OFFSET = [112,107]
    WIZARD_DATA = [WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]


    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
        screen.blit(scaled_bg,(0,0))
    
    def draw_health_bars(health, x, y):
        ratio = health/100
        pygame.draw.rect(screen,WHITE,(x-3,y-3,405,28),border_radius=10)
        pygame.draw.rect(screen,RED,(x,y,400,20),border_radius=10)
        pygame.draw.rect(screen,YELLOW,(x,y,400*ratio,20),border_radius=10)

    #Create Fighters
    fighter_1 = Fighter(200,310,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEPS,sword_fx,running)
    fighter_2 = Fighter(700,300,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_SETPS,magic_fx,running)

    run = True
    win = 0
    while run:
        clock.tick(FPS)
        draw_bg()
        draw_health_bars(fighter_1.health, 20,20)
        draw_health_bars(fighter_2.health, 580,20)
        
        fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
        fighter_1.update()
        fighter_1.draw(screen)
        # fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
        fighter_2.update()
        fighter_2.draw(screen)
        
        if(fighter_2.health <= 0):
            if win ==0:
                you_win.play()
                win = 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.flip()

    pygame.quit()
    
main_game()
