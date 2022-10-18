

from loaders.load_wizard import load_wizard
from loaders.load_ninja import load_ninja
from loaders.load_marshal import load_martial_arts
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
    
    #custom characters
    knight_images = load_knight()
    martial_images = load_martial_arts()
    ninja_images = load_ninja()
    mage_images = load_wizard()

    print(mage_images)
    
    pygame.display.set_caption("Brawllar")

    bg_image = pygame.image.load("assets/images/background/bg4.jpg").convert_alpha()
    warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
    wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()
    sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
    sword_fx.set_volume(0.1)
    magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
    magic_fx.set_volume(0.1)
    running = pygame.mixer.Sound("assets/audio/running.mp3")
    
    you_win = pygame.mixer.Sound("assets/audio/you-win.mp3")
    you_win.set_volume(0.1)

    battle_ready = pygame.mixer.Sound("assets/audio/battle-ready.mp3")
    battle_ready.set_volume(0.1)
    pygame.mixer.music.load("assets/audio/music.mp3")
    # pygame.mixer.music.play(-1,0.0,5000)
    WARRIOR_ANIMATION_STEPS = [10,8,1,7,7,3,7]
    WIZARD_ANIMATION_SETPS = [8,8,1,8,8,3,7]

    KNIGHT_ANIMATION_STEPS = [11,8,4,6,6,4,9]
    KNIGHT_SIZE = 140
    KNIGHT_SCALE = 4
    kNIGHT_OFFSET= [62,30]
    KNIGHT_DATA = [KNIGHT_SIZE,KNIGHT_SCALE,kNIGHT_OFFSET]

    #Martial

    MARTIAL_ANIMATION_STEPS = [10,8,3,7,6,3,11]
    MARTIAL_SIZE = 126
    MARTIAL_SCALE = 4
    MARTIAL_OFFSET = [50,30]
    MARTIAL_DATA = [MARTIAL_SIZE,MARTIAL_SCALE,MARTIAL_OFFSET]


    #Ninja

    NINJA_ANIMATION_STEPS = [4,8,2,4,4,3,7]
    NINJA_SIZE = 200
    NINJA_SCALE = 4
    NINJA_OFFSET = [90,80]
    NINJA_DATA=[NINJA_SIZE,NINJA_SCALE,NINJA_OFFSET]


    #WIZZI
    MAGE_ANIMATION_STEPS = [6,8,2,8,8,4,7]
    MAGE_SIZE = 231
    MAGE_SCALE=2
    MAGE_OFFSET=[90,70]
    MAGE_DATA = [MAGE_SIZE,MAGE_SCALE,MAGE_OFFSET]


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
    fighter_1 = Fighter(200,300,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEPS,sword_fx,running)
    fighter_2 = Fighter(700,300,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_SETPS,magic_fx,running)
    fighter_3 = Fighter(200,300,True,KNIGHT_DATA,knight_images,KNIGHT_ANIMATION_STEPS,sword_fx,running,different=True)
    fighter_4 = Fighter(200,300,True,MARTIAL_DATA,martial_images,MARTIAL_ANIMATION_STEPS,sword_fx,running,different=True)

    fighter_5 = Fighter(200,300,True,NINJA_DATA,ninja_images,NINJA_ANIMATION_STEPS,sword_fx,running,different=True)
    fighter_6 = Fighter(700,300,False,MAGE_DATA,mage_images,MAGE_ANIMATION_STEPS,magic_fx,running,different=True,height=190)

    player_1 = fighter_5
    player_2 = fighter_6

    player_2.x = 700
    player_2.set_as_p2()
    run = True
    win = 0
    battle_ready.play()
    while run:
        clock.tick(FPS)
        draw_bg()
        draw_health_bars(player_1.health, 20,20)
        draw_health_bars(player_2.health, 580,20)
        
        player_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,player_2)
        player_1.update()
        player_1.draw(screen)
        player_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,player_1)
        player_2.update()
        player_2.draw(screen)
        
        if(player_2.health <= 0 or player_1.health <=0):
            if win ==0:
                you_win.play()
                win = 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.flip()

    pygame.quit()
    
main_game()
