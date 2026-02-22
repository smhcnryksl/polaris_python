class Asistan:
    
    def __init__(self, isim):
        self.isim = isim
        self.islem_sayisi = 0
        
    def selam_ver(self, kullanici_adi):
        print(f"Merhaba {kullanici_adi}, ben {self.isim}. Sana nasıl yardım edebilirim?")
        self.islem_sayisi += 1
        
    
    def durum_raporu(self):
        print(f"Bugüne kadar toplam {self.islem_sayisi} işlem gerçekleştirdim.")
        

asistan1 = Asistan("a")
asistan1.selam_ver("semih")
asistan1.durum_raporu()