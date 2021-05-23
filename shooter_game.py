#Создай собственный Шутер!
from random import randint
from pygame import *
import pygame
win=display.set_mode((800,600))
display.set_caption("ok")
back=transform.scale(image.load("galaxy.jpg"),(800,600))
x1=400
y1=500
if game:
    mixer.init()
    mixer.music.load("space.ogg")
    mixer.music.play()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,j1,j2,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.j1=j1
        self.j2=j2
        self.player_image=player_image
        self.image=transform.scale(image.load(self.player_image),(self.j1,self.j2))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def spawn(self):
            win.blit(self.image,(self.rect.x,self.rect.y))
class player(GameSprite):
    def dwigatsa_w_levo(self):
        if self.rect.x > 0 :
            self.rect.x -=self.speed
    def dwigatsa_w_prawo(self):
        if self.rect.x < 700 :
            self.rect.x +=self.speed
sp1=player(75,100,"rocket.png",x1,y1,10)
top=sp1.rect.top
class bullet(GameSprite):
    def update(self):
        self.rect.x=top
        self.rect.y-=self.speed
        if self.rect.y < 0:
            self.rect.y=425
            b1.kill()
    def shoot(self):
        bullets.add(b1)
b1=bullet(10,20,"bullet.png",x1,top,10)
bullets=pygame.sprite.Group()
class wrag(GameSprite):
    def update(self):
        self.speed=randint(1,10)
        self.rect.y+=self.speed
        if self.rect.y > 600:
            self.rect.y=0
            self.rect.x=randint(1,600)
wragi=pygame.sprite.Group()
for i in range(6):
    w1=wrag(100,65,"ufo.png",randint(1,770),0,randint(5,10))
    wragi.add(w1)
mixer.init()
mixer.music.load("fire.ogg")
game = True
fps=60
clock=time.Clock()
clock.tick(fps)
while game == True:
    win.blit(back,(0,0))
    sp1.spawn()
    wragi.update()
    wragi.draw(win)
    bullets.draw(win)
    bullets.update()
    display.update()
    key_p=key.get_pressed()
    if key_p[K_SPACE]:
        bullets.add(b1)
        mixer.music.play()
    if key_p[K_a]:
        sp1.dwigatsa_w_levo()
    if key_p[K_d]:
        sp1.dwigatsa_w_prawo()
    for e in event.get():
        if e.type == QUIT:
            game=False
    clock.tick(fps)