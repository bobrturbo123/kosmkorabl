import sys
import pygame
import random


randomnum =  random.randint(1,250)

class Sprites:
    def __init__(self,name_image, x, y, width, height):
        self.image = pygame.image.load(name_image)
        self.image=pygame.transform.scale(self.image,(width,height))
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y = y

    def draw_image(self): #МЕТОД!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        screen.blit(self.image, (self.rect.x,self.rect.y)) #это отрисовка картинок на координатах x и y


    def colide_food(self,f):
      if self.rect.colliderect(f.rect) == True:
          return 1




    def move_kosmkorabl(self):#метод!!!!!!!!!!!!!!!!!!!!
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 10



    def shoot_enemy(self,randomnum,i):
        if randomnum == 12:
            bulleten = Sprites('снаряд.png', i.rect.x+20, i.rect.y + 30, 30, 45)
            bulet_enemy.append(bulleten)


    def enemy_bulet(self):
        self.rect.y += 5



pygame.init()
window_size = (1280, 720)
life = 3
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Spase Batle")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера

kosmkorabl=Sprites('Корабль-Photoroom.png', 490,500, 200, 98)
fon=Sprites("cosmos_1.png",0,0,1280,720)
enemy1=Sprites("монстрик-Photoroom.png",100,100,64,64)
enemy6=Sprites("монстрик-Photoroom.png",200,100,64,64)
enemy7=Sprites("монстрик-Photoroom.png",300,100,64,64)
enemy8=Sprites("монстрик-Photoroom.png",400,100,64,64)
enemy2=Sprites("монстрик-Photoroom.png",500,100,64,64)
enemy9=Sprites("монстрик-Photoroom.png",600,100,64,64)
enemy3=Sprites("монстрик-Photoroom.png",700,100,64,64)
enemy4=Sprites("монстрик-Photoroom.png",800,100,64,64)
enemy10=Sprites("монстрик-Photoroom.png",900,100,64,64)
enemy11=Sprites("монстрик-Photoroom.png",1000,100,64,64)
enemy12=Sprites("монстрик-Photoroom.png",1100,100,64,64)
enemy5=Sprites("монстрик-Photoroom.png",1200,100,64,64)
enemy13=Sprites("монстрик-Photoroom.png",0,100,64,64)


serdce1=Sprites("сердце.png",0,0,50,40)
serdce2=Sprites("сердце.png",60,0,50,40)
serdce3=Sprites("сердце.png",120,0,50,40)


enemy_list = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10,enemy11,enemy12,enemy13]
serdce_list=[serdce1,serdce2,serdce3]
bulets =[]
bulet_enemy=[]

lifes = 3
backgound_color = (0,0,255) #цвет
textik = "you lose"
x = 0
clr = (255,255,255)
font = pygame.font.SysFont('Arial',50)
text = font.render(textik,True, clr)
hp = 3
while True:  # игрововй таймер
    randomnum = random.randint(1, 250)
    clock.tick(40)  # частота обновления таймераааааа
    fon.draw_image()

    for i in serdce_list:
        i.draw_image()
        if lifes != hp:
            serdce_list.pop()
            hp = hp - 1
    for i in bulets:
        i.draw_image()
        i.rect.y -= 10
        for j in enemy_list:
            if i.rect.colliderect(j.rect):
                enemy_list.remove(j)
                bulets.remove(i)

    for i in enemy_list:

        i.draw_image()
        i.colide_food(kosmkorabl)
        i.shoot_enemy(randomnum,i)
        randomnum = random.randint(1, 250)
        x = i.colide_food(kosmkorabl)
        if x == 1 :
            enemy_list.remove(i)
        x=0



    for i in bulet_enemy:
        i.draw_image()
        i.enemy_bulet()
        if i.rect.colliderect(kosmkorabl.rect):
            lifes = lifes - 1
            bulet_enemy.remove(i)


    kosmkorabl.draw_image()
    kosmkorabl.move_kosmkorabl()




    if lifes <= 0:
        screen.fill(backgound_color)
        screen.blit(text,(500,500))
        for event in pygame.event.get():  # проходимся по событиям
            if event.type == pygame.KEYDOWN:
                sys.exit()


    if enemy_list == []:
        screen.fill(backgound_color)
        textik = "you win!"
        text = font.render(textik, True, clr)
        screen.blit(text,(500,500))
        for event in pygame.event.get():  # проходимся по событиям
            if event.type == pygame.KEYDOWN:
                sys.exit()


    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Sprites('снаряд.png',kosmkorabl.rect.x+89,kosmkorabl.rect.y+30,30,45)
            bulets.append(bullet)
        if event.type == pygame.QUIT:  # если нажали на крестик
            sys.exit()  # выйти
    pygame.display.update() #ОБНОВЛЕНИЕ ДИСПЛЕЯ