class Roket:
    def __init__(self, isim, yakit_seviyesi):
        self.isim = isim
        self.yakit_seviyesi = yakit_seviyesi
    
    
    def yakit_doldur(self, miktar):
        self.yakit_seviyesi += miktar
        print(f"Yakıt eklendi. Yeni seviye: {self.yakit_seviyesi}")
        
    
    def firlat(self):
        if self.yakit_seviyesi > 10:
            print("Roket başarıyla fırlatıldı 🌍 -> ☀️")
            self.yakit_seviyesi -= 10
        else:
            print("Hata: Yetersiz yakıt! Lütfen yakıt doldurun.")
            
            
            
roket1 = Roket("Semih", 8)
roket1.yakit_doldur(1)
roket1.firlat()

