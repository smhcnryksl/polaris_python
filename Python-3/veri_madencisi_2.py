import re

veriler = []
veri = []

with open("lvl2_bozuk_veri.txt", encoding="utf-8") as file:

    pattern_mail = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    pattern_tel = re.compile(r"\+?\(?\d{0,3} ?\(?\d{3}\)?[ -]\d{3}[ -]?\d{2}[ -]?\d{2}")

    for line in file:
        mail = pattern_mail.findall(line)
        tel = pattern_tel.findall(line)
        veri = tel + mail
        veriler.extend(veri)



with open("lvl2_temiz_rehber.txt", "a") as f:
    for veri in veriler:
        if veri:
            f.write(f"{veri.strip()}\n")
