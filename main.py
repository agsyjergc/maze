import pygame
class GSprite(pygame.sprite.Sprite):
    def __init__ (self,sprite_immage,x,y,speed,w,h):
        super().__init__()
        self.sprite_immage = pygame.transform.scale(pygame.image.load(sprite_immage),(w,h))
        self.rect = self.sprite_immage.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def appear(self):
        okno.blit(self.sprite_immage, (self.rect.x, self.rect.y))
class Player(GSprite):
     def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and self.rect.x  < 650:
            self.rect.x += self.speed
        if key[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key[pygame.K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if key[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            
class Enemy(GSprite):
    direction = 'left'
    def walk(self,x1,x2):
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x <= x1:
                self.direction = 'right'

        if self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x >= x2:  
                self.direction = 'left' 
            #Киборг не отображается, а self.rect.x меняется  
class wall(pygame.sprite.Sprite):
    def __init__(self, color1, color2, color3, wx,wy,width, hight):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.hight = hight
        self.image = pygame.Surface((self.width , self.hight))
        self.rect = self.image.get_rect()
        self.rect.x = wx
        self.rect.y = wy
        self.image.fill((color1,color2,color3))
    def draww(self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
Wall_1 = wall(240, 201, 10,80,20,10,350)
Wall_2 = wall(240, 201, 10,80,20,560,10)
Wall_3 = wall(240, 201, 10,80,450,10,70)
Wall_4 = wall(240, 201, 10,640,20,10,490)
Wall_5 = wall(240, 201, 10,510,300,10,490)
Wall_6 = wall(240, 201, 10,80,100,100,10)
Wall_7 = wall(240, 201, 10,170,100,10,300)
Wall_8 = wall(240, 201, 10,400,400,10,350)
Wall_9 = wall(240, 201, 10,280,400,120,10)
Wall_10 = wall(240, 201, 10,280,100,10,300)
Wall_11 = wall(240, 201, 10,400,20,10,300)
Wall_12 = wall(240, 201, 10,510,210,130,10)
Wall_13 = wall(240, 201, 10,510,120,10,100)
pygame.mixer.init()
pygame.mixer.music.load('New Look.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
okno = pygame.display.set_mode((700,500))
pygame.display.set_caption('Лабиринт')
#задай фон сцены


background = pygame.transform.scale(pygame.image.load('honey combs.jpg'),(700,500))
Hero = Player('bee.png',20,370,5,50,50)
Bread = GSprite('treasure.png',560,435,0,50,50)
Cyborg = Enemy('cyborg.png',520,300,1,50,50)

#создай 2 спрайта и размести их на сцене
#обработай событие «клик по кнопке "Закрыть окно"»
a = True
s = False
pygame.font.init()
kick = pygame.mixer.Sound('kick.ogg')
loaf = pygame.mixer.Sound('money.ogg')
font  = pygame.font.SysFont('constantia', 100)
text = font.render('Вы проиграли', True, (137, 52, 235))
text1 = font.render('Вы выиграли', True, (137, 52, 235))
#Cyborg.walk(520,580)
clock = pygame.time.Clock()
while a:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            a = False
    if s != True:
        okno.blit(background,(0,0))
        Wall_1.draww()
        Wall_2.draww()
        Wall_3.draww()
        Wall_4.draww()
        Wall_5.draww()
        Wall_6.draww()
        Wall_7.draww()
        Wall_8.draww()
        Wall_9.draww()
        Wall_10.draww()
        Wall_11.draww()
        Wall_12.draww()
        Wall_13.draww()
        Hero.appear()
        Bread.appear()
        Hero.move()
        Cyborg.walk(520,580)
        Cyborg.appear()
        if pygame.sprite.collide_rect(Hero,Cyborg) or pygame.sprite.collide_rect(Hero,Wall_1) or pygame.sprite.collide_rect(Hero,Wall_2) or pygame.sprite.collide_rect(Hero,Wall_3) or pygame.sprite.collide_rect(Hero,Wall_4) or pygame.sprite.collide_rect(Hero,Wall_5) or pygame.sprite.collide_rect(Hero,Wall_6) or pygame.sprite.collide_rect(Hero,Wall_7) or pygame.sprite.collide_rect(Hero,Wall_8) or pygame.sprite.collide_rect(Hero,Wall_9) or pygame.sprite.collide_rect(Hero,Wall_10) or pygame.sprite.collide_rect(Hero,Wall_11) or pygame.sprite.collide_rect(Hero,Wall_12) or pygame.sprite.collide_rect(Hero,Wall_13):
            okno.blit(text, (20,200) )
            s = True
            kick.play()
        if pygame.sprite.collide_rect(Hero,Bread):
            loaf.play()
            okno.blit(text1, (20,200) )
            s = True
    















    pygame.display.update()
    clock.tick(60)
