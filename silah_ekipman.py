import random



class S_Ekipman():
    def __init__(self,hasar,crit=0,zirhdelme=0,infaz=0,kanatma=0):
        self.hasar = hasar
        self.crit = crit # 0 - 100 // 100> = dmg multiplayer
        self.zirhdelme = zirhdelme  # 1 = 10% ,10 = 100%
        self.infaz = infaz   # 1 = 10%, 5= 50%
        self.kanatma = kanatma   # kanama süresi (tur)
        self.kanamabaslat = False
        # 2: zehirleme
        # 3: can çalma

    def infazet(self,hedef):
        hedefcanoranı = 100 * hedef.can / hedef.maxcan
        if hedefcanoranı <= self.infaz * 10 and hedefcanoranı != 0:
            hedef.can = 0
            return 1
        
    def critheck(self):
        chance = random.randint(1, 100)
        if self.crit > 100:
             wowdamage = self.silah.crit/100
             return wowdamage
            
        elif chance <= self.crit or self.crit == 100:
            return 1
        else:
            return 0
    
    def kanat(self,hedef):
        if self.kanatma > 0 and self.kanamabaslat is True:
            hedef.kanama = self.kanatma
            hedef.can = hedef.can - self.kanatma
        return hedef


    


        


test_yumruk = S_Ekipman(hasar=10,kanatma=1)
yumruk = S_Ekipman(hasar=10)
kiliç = S_Ekipman(hasar=25,crit=10)
bıçak = S_Ekipman(hasar=20,crit=10)
