import re

def main():
    sifre = input("Şifre girin: ")
    print(validate(sifre))



def validate(sifre):
    pattern = re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[-_+@$!%*?&#]).{8,}$")
    if not sifre.strip():
        return "Eksik şifre"
    elif re.search(pattern, sifre):
        return "Şifre onaylandı"
    else:
        return "Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir."
    

if __name__ == "__main__":
    main()