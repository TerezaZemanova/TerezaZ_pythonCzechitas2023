def over_format (prijemce):
    if "+420" not in prijemce:
        spravny_format = ("+420" + prijemce)
    if len(spravny_format) == 13:
       spravny_format
    else:
        print("Nespravny format cisla.")

    return spravny_format

prijemce = input("Zadejte cislo prijemce: ")
telefon = over_format(prijemce)
print (f"Vaše číslo je {telefon}")

def zpocitej_cenu (zprava):
    delka_zpravy = len(zprava)
    cena_za_180 = 3
    celkova_cena = (delka_zpravy // 180) * cena_za_180

    if delka_zpravy % 180 > 0:
        celkova_cena += cena_za_180

    return celkova_cena

zprava = input("Zadejte zpravu: ")
cena = zpocitej_cenu(zprava)
print(f"Vaše zpráva stojí {cena} Kc.")
