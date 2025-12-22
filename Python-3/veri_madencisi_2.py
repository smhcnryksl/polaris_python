import re

# Telefon numarası ve mail için pattern
pattern_mail = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
pattern_tel = re.compile(r"\+?\(?\d{0,3} ?\(?\d{3}\)?[ -]\d{3}[ -]?\d{2}[ -]?\d{2}")

veriler = []

# Telefon numarası standartlaştırma işlemi
def tel_temizle(tel):
    temiz = re.sub("[^\d+]", " ", tel)
    temiz = temiz.replace("  ", " ")
    temiz = temiz.strip()

    # Son 4 karakteri 2'li gruplara ayırma
    if temiz[-3] != " ":
        ilk = temiz[:-2]
        iki = temiz[-2:]
        temiz = ilk + " " + iki

    # Ülke kodu kontrolü ve eklenmesi
    if len(temiz) == 13:
        return f"+90 {temiz}"

    elif temiz[0] == "0" and len(temiz) >= 10:
        return f"+90 {temiz[1:]}"
    else:
        return temiz


# Metinden verileri çekme
with open("lvl2_bozuk_veri.txt", encoding="utf-8") as file:
    for line in file:
        mail = pattern_mail.findall(line)
        tel = pattern_tel.findall(line)
        for t in tel:
            telefon = tel_temizle(t)
            if telefon not in veriler:
                veriler.append(telefon)
            else:
                continue

        for m in mail:
            veriler.append(m)

# Temizlenmiş bilgileri yeni dosyaya yazar
with open("lvl2_temiz_rehber.txt", "w") as f:
    for veri in veriler:
        if veri:
            f.write(f"{veri}\n")
