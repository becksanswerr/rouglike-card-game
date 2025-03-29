import os
from karakter import karakter
from silah_ekipman import *
from zirh_ekipman import *



savaşçi = karakter("savasçi",
                can=200,
                silah=test_yumruk,
                kalkan_gücü=30
                )

hirsiz = karakter("hirsiz",
                can=150,
                silah=bıçak,
                kalkan_gücü=20
                )


def kazanankim(self,rakip):
    if rakip.can <= 0 and self.can <= 0:
                print("berabere!")
                exit()
    elif rakip.can <= 0:
                print(f"{self.adi}, kazandi!")
                exit()
    elif self.can <= 0:
                print(f"{rakip.adi}, kazandi!")
                exit()

        
def savas(self,rakip):
    tur = 0
    os.system("cls")
    print(f"tur: {tur}")
    self.canbari.draw()
    rakip.canbari.draw()
    input()

    
    hak1 = self.hiz
    hak2 = 0
    while 1:
        os.system("cls")
        tur += 1
        print(f"tur: {tur}")
        self.sinirlimi()

        self.canbari.draw()
        rakip.canbari.draw()
        

        if hak1 > 0 and hak2 == 0: 
            seçenek = input("saldır / savun :")
            if seçenek == "saldir":
                ad,dmg = self.vur(rakip)
            else:
                ad, dmg = self.savun()
            


            hak1 -= 1
            if hak1 == 0:
                   hak2 = rakip.hiz
        else:
            if hak2 > 0 and hak1 == 0:
                seçenek = input("saldir / savun :")
                if seçenek == "saldir":
                    ad,dmg = rakip.vur(self)
                else:
                    ad,dmg = rakip.savun()

                hak2 -= 1
                if hak2 == 0:
                       hak1 = self.hiz


        kan1 = self.silah.kanat(rakip)
        kan2 = rakip.silah.kanat(self)

        os.system("cls")
        print(f"tur: {tur}")
        self.canbari.draw()
        rakip.canbari.draw()
        print(f"{ad}" f" {int(dmg)}" " hasar yedi! \n"
              f"{str(kan1.adi) + ' kaniyor '+'('+ str(kan1.kanama) +')' if kan1.kanama > 0 else ''}"
              f"{str(kan2.adi) + ' kaniyor '+'('+ str(kan1.kanama) +')' if kan2.kanama > 0 else ''}")
              
        kazanankim(self,rakip)
        input()


savas(savaşçi,hirsiz)