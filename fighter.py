
import pygame

class Fighter():
    
    def __init__(self,x,y,flip:bool,data,sprite_sheet,animation_steps,sound,running:pygame.mixer.Sound) -> None:
        self.size = data[0]
        self.scale = data[1]
        self.offset = data[2]
        self.rect = pygame.Rect((x,y,80,180))
        self.animation_list = self.load_images(sprite_sheet,animation_steps)
        self.vel_y  = 0
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.jumping = False 
        self.attacking = False 
        self.hit = False
        self.running_sound = running
        self.health = 100
        self.update_time = pygame.time.get_ticks()
        self.flip = flip
        self.attack_cooldown = 0
        self.running = False
        self.attack_sound = sound
        self.alive = True
     
        
    
    def load_images(self,sprite_sheet:pygame.Surface,animation_steps):
        animation_list = []
        for y,animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x* self.size,y* self.size,self.size,self.size)
               
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size * self.scale, self.size* self.scale)))
            animation_list.append(temp_img_list)
        
        return animation_list
    def move(self,screen_width,screen_height,surface,target:'Fighter'):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.attack_type = 0
        self.running = False
        #get keypress
       
        
        key = pygame.key.get_pressed()
        
        #Check for movement
        #can only perform other action if not attacking
        if self.attacking is False:
            if key[pygame.K_a]:
                self.running = True
               
              
                dx = -SPEED
            if key[pygame.K_d]:
                self.running = True
                dx = SPEED
                # self.running_sound.play()
                
            #jump
            
            if key[pygame.K_w] and not self.jumping:
                self.jumping = True
                self.vel_y = -30
                
            if key[pygame.K_q] or key[pygame.K_e]:
                #determine which key was pressed
                self.attack(surface,target)
                if key[pygame.K_q]:
                    
                    self.attack_type = 1
                if key[pygame.K_e]:
                    self.attack_type = 2
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -=1
        
        self.vel_y += GRAVITY
        dy += self.vel_y
            
        #ensure player is on screen
        
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        
        
        if self.rect.bottom + dy > screen_height -110:
            self.jumping= False
            self.vel_y = 0
            dy = screen_height -110 - self.rect.bottom

        #ensure player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip =True
            
        self.rect.x += dx
        self.rect.y += dy
    
    
    def attack(self,surface,target:'Fighter'):
   
        if self.attack_cooldown != 0:
            return
        self.attack_sound.play()
        self.attacking=True
        attacking_rect = pygame.Rect(self.rect.centerx -(2* self.rect.width * self.flip), self.rect.y, 2* self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 35
            target.hit = True
            
            
        pygame.draw.rect(surface,(0,255,0),attacking_rect)
    
    def update(self):
        #Check what action the player is performing 
        if self.health <=0:
            self.health = 0
            self.alive = False
            self.update_action(6)
        elif self.hit == True:
            self.update_action(5)
        elif self.attacking:
            if self.attack_type==1:
                self.update_action(3)
            elif self.attack_type ==2:
                self.update_action(4)
        elif self.jumping:
            self.update_action(2)
        elif self.running:
            self.update_action(1)
        else:
            self.update_action(0)
        animation_cooldown = 100
        
        self.image = self.animation_list[self.action][self.frame_index]  
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        
        if self.frame_index >= len(self.animation_list[self.action]):
            
            #if the player is dead.
            if self.alive == False:
                 self.frame_index = len(self.animation_list[self.action])-1
            else:
            
                self.frame_index = 0
                
                #check if the attack was execute
                
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 50
                
                if self.action == 5:
                    self.hit=False
                    
                    #if the player was in the middle of the attack the attack was stopped
                    
                    self.attacking = False
                    self.attack_cooldown = 20
          
    def draw(self,surface:pygame.Surface):
        img = pygame.transform.flip(self.image, self.flip,False)
        # pygame.draw.rect(surface,(0,0,255),self.rect)
        surface.blit(img,(self.rect.x - (self.offset[0] * self.scale) ,self.rect.y - (self.offset[1]* self.scale)))
        
    
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()