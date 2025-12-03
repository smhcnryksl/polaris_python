sayi = float(input("Bir sayı girin: "))
print()

if sayi == 0:
    print("Giridğiniz sayı 0.")
elif sayi > 0:
    print(f"Girdiniz {sayi:g} sayısı pozitif bir sayı.")
else:
    print(f"Gridiniz {sayi:g} sayısı negatif bir sayı")