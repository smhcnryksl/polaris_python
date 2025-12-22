from sifre_güvenligi import validate


def test_buyuk_harf():
    assert validate("tumhepsi_kucuk1") == False
    assert validate("follow_the_white_ra66it") == False


def test_kisa_sifre():
    assert validate("Kisa*9") == False
    assert validate("Budha_1") == False


def test_whitespace():
    assert validate("   ") == False
    assert validate("") == False


def test_sayi_kontrol():
    assert validate("Rakam_Koymadım") == False
    assert validate("+WakeUpNeo") == False


def test_ozel_karakter_kontrolu():
    assert validate("Busifredeozelyok1") == False


def test_guclu_sifre():
    assert validate("I_Love_CS50P") == True
    assert validate("Stem_Has_No_Limits_2018") == True
