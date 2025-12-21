from sifre_güvenligi import validate


def test_validate():
    assert validate("Rakam_Koymadım") == "Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir."
    assert validate("tumhepsi_kucuk1") == "Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir."
    assert validate("busifredeozelyok1") == "Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir."
    assert validate("bukisa") == "Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir."
    assert validate("WakeUpNeo") == "Güçsüz şifre! Şifreniz en az 1 büyük harf, 1 sayı, ve 1 özel karakter(- _ + # @ $ ! % * ? &) içermelidir."
    assert validate("   ") == "Eksik şifre"
    assert validate("I_Love_CS50P") == "Şifre onaylandı"
    assert validate("Stem_Has_No_Limits_2018") == "Şifre onaylandı"
