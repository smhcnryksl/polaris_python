import re


def main():
    sifre = input("Şifre girin: ")
    print(validate(sifre))


def validate(sifre):
    pattern = re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[-_+@$!%*?&#]).{8,}$")
    if not sifre.strip():
        print("Eksik Şifre")
        return False
    elif re.search(pattern, sifre):
        print("Şifre Onaylandı")
        return True
    else:
        print("Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir")
        return False


if __name__ == "__main__":
    main()
