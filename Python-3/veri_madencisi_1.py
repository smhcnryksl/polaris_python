import re


def tel_temizle(tel):
    temiz = re.sub("[^\d+]", " ", tel)

    if temiz[-3] != " ":
        ilk = temiz[:-2]
        iki = temiz[-2:]
        temiz = ilk + " " + iki

    if temiz[0] == "0" and len(temiz) >= 10:
        return f"+90 {temiz}"
    else:
        return temiz


veriler = []
veri = []


with open("lvl1_bozuk_veri.txt", encoding="utf-8") as file:

    pattern_mail = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    pattern_tel = re.compile(r"\+?\d{1,3} ?\(?\d{3}\)? \d{3} ?-?\d{2} ?\d{2}")

    for line in file:
        mail = pattern_mail.findall(line)
        tel = pattern_tel.findall(line)
        for t in tel:
            telefon = tel_temizle(t)
            veriler.append(telefon)

        for m in mail:
            veriler.append(m)


with open("lvl1_temiz_rehber.txt", "a") as f:
    for veri in veriler:
        if veri:
            f.write(f"{veri}\n")
