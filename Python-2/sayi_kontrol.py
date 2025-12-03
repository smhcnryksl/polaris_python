while True:
    sayi = input("Sayı giriniz: ")
    try:
        sayi = float(sayi)
        print("Girdiğiniz sayı geçerlidir.")
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")