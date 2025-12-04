import datetime


tarih = input("Vizelerinizin tarihini GG.AA.YYYY formatında girin: ")
zaman = input("Vizelerinizin saatini SS.DD formatında girin: ")

gun, ay, yil = tarih.split(".")
saat, dakika = zaman.split(".")

gun = int(gun)
ay = int(ay)
yil = int(yil)
saat = int(saat)
dakika = int(dakika)

vize = datetime.datetime(yil, ay, gun, saat, dakika)
suan = datetime.datetime.now()

fark = vize - suan
toplam_saniye = int(fark.total_seconds())

kalan_gun = toplam_saniye // 86400
kalan_saniye = toplam_saniye % 86400
kalan_saat = kalan_saniye // 3600
kalan_saniye = kalan_saniye % 3600
kalan_dakika = kalan_saniye // 60

print(f"{kalan_gun} gün, {kalan_saat} saat ve {kalan_dakika} dakika sonra vizeleriniz başlıyor.")



