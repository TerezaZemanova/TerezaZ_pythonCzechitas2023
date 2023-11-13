class auto: 
    def __init__(self, registracni_znacka: float, znacka: str, typ_vozidla: float, najete_km: float, dostupne: str):
        self.atribut_SPZ = registracni_znacka
        self.atribut_znacka = znacka
        self.atribut_typ = typ_vozidla
        self.atribut_km = najete_km
        self.atribut_dostupne = dostupne

    def pujc_auto(self):
        if self.atribut_dostupne == "volne":
            return "Potvrzuji zapůjčení vozidla."
        else:
            self.atribut_dostupne = "pujcene"
            return "Vozidlo není k dispozici."

    def get_info(self):
        return f"Informace o vozidle: SPZ {self.atribut_SPZ}, značka {self.atribut_znacka}, typ vozidla {self.atribut_typ}."

auto1 = auto("4A2 3020", "Peugeot", "403 Cabrio", "47534", "volne")
auto2 = auto ("1P3 4747", "Škoda", "Octavia", "41253", "volne")

vypujceni = input("Zadejte značku požadovaného vozidla (peugeot/škoda): ")
if vypujceni == "peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
else: 
    print(auto2.get_info())
    print(auto2.pujc_auto())
