class Dedektif:
    def __init__(self):
        self.supheliler = ["Albay Mustard", "Profesör Plum", "Bayan Scarlet"]

    def supheli_ele(self, isim):
        if isim in self.supheliler:
            self.supheliler.remove(isim)
        else:
            pass
    def suclu_kim(self):
        kalan_sayisi = len(self.supheliler)
        
        if kalan_sayisi == 1:
            print(f"Kesin bilgi, suçlu bulundu: {self.supheliler[0]}")
        elif kalan_sayisi > 1:
            print("Henüz yeterli kanıt yok.")
        else:
            print("Mantık hatası: Herkes elendi!")
