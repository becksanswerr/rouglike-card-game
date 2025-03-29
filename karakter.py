import random
import pygame
from silah_ekipman import *
from zirh_ekipman import *

class karakter():
    def __init__(self,color,x,y,adi,can,silah=0,enerji=10,zirh=0,sinir=0,kalkan_gücü=0):
        self.x, self.y = x,y
        self.color = color
        self.enerji = enerji

        self.adi = adi

        if silah is 0:
            silah = yumruk
        self.silah = silah
        
        if zirh is 0:
            zirh = ciplak
        self.zirh = zirh

        self.kalkan_gücü = kalkan_gücü
        self.kalkan = 0
        self.can = can 
        self.maxcan = can
        
  

        self.sinir = sinir # canın altı: 1 = 10% ,5 = 50% (hasar x2)
        self.sinirli = False

        self.kanama = 0
        self.zehirli = 0



    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))
        font = pygame.font.Font(None, 24)
        hp_text = font.render(f"Can: {self.can} | Kalkan: {self.kalkan}", True, (255, 255, 255))
        name_text= font.render(self.adi, True, (255, 255, 255))
        screen.blit(name_text, (self.x, self.y - 85))
        screen.blit(hp_text, (self.x, self.y - 55)) 


        ratio = self.can / self.maxcan
        pygame.draw.rect(screen, "red", (self.x, self.y - 30, 100, 20))
        pygame.draw.rect(screen, "green", (self.x, self.y - 30, 100 * ratio, 20))
        

    def test(self):
        print(self.kaniyor)


    def silah_kuşan(self,yeni_ekipman):
        self.silah = yeni_ekipman

         

    def sinirlimi(self):
        canoranı = max(0.1 , 100 * self.can / self.maxcan)
        siniroranı = self.sinir * 10
        if canoranı <= siniroranı and self.sinirli == False:
            self.silah.hasar = self.silah.hasar * 2
            self.sinirli = True
            print(f"{self.adi} SİNİRLENDİ!!!")

    def savun(self):
        self.kalkan = self.kalkan_gücü
        return self.adi, self.kalkan
             
    def vur(self,hedef):
        
        hasar = self.silah.hasar
        hedef_zirh = hedef.zirh.koruma
        zirhdelme = self.silah.zirhdelme

        hasar_azaltma = hasar * ((hedef_zirh - zirhdelme) * 10 / 100)
        top_hasar = hasar - hasar_azaltma

        crit = self.silah.critheck()
        if crit >= 1:
            son_hasar = max(0, (top_hasar + (top_hasar * 0.5 * crit)))

        elif crit == 0:
            son_hasar = max(0, top_hasar)


        kalan_hasar = hedef.kalkan - son_hasar

        sonuc = hedef.can - abs(kalan_hasar)

        if kalan_hasar <= 0:
            hedef.kalkan = max(kalan_hasar,0)
            hedef.can = max(sonuc, 0)
        if kalan_hasar > 0:
            hedef.kalkan = max(kalan_hasar,0)

        self.silah.kanamabaslat == True
        self.silah.infazet(hedef)
        hedef.sinirlimi()
        
        return hedef.adi,son_hasar




