try:
    sayi_1 = int(input("Birinci sayıyı girin: "))
    sayi_2 = int(input("İkinci sayıyı girin: "))
    print()
    print(f"toplam: {sayi_1 + sayi_2}")
    print(f"fark: {sayi_1 - sayi_2}")
    print(f"çarpım: {sayi_1 * sayi_2}")
    print(f"bölüm: {sayi_1/sayi_2:g}")
except ZeroDivisionError:
    print("bir sayı 0 ile bölünemez")