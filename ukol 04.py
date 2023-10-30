# Nechce mi to vyhodit else, nevím proc :-(

prijemce = input("Zadejte cislo prijemce: ")

if "+420" not in prijemce:
    spravny_format = "+420" + prijemce
    print(f"Cislo prijemce je {spravny_format}.")
elif len(prijemce) == 9 or len(prijemce) == 13:
    spravny_format = prijemce
else:
    print("Nespravny format cisla.")

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
