import random

sayi = random.randint(1, 100)
deneme = 0

while True:
    girdi = int(input("1 ve 100 de dahil olmak üzere bu aralıkta bir sayı giriniz: "))

    if girdi == sayi:
        print(f"Tebrikler {deneme} denemede doğru tahmin ettiniz 🏆"),
        break
    elif girdi < sayi:
        print("Daha yüksek")
        deneme += 1
        continue
    elif girdi > sayi:
        print("Daha düşük")
        deneme += 1
        continue

