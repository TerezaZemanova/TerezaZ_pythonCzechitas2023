sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

pozadovana_soucastka = (input("Zadejte kod soucastky: "))

if pozadovana_soucastka not in sklad:
    print ("Soucastka neni skladem.")
else:
    pozadovane_mnozstvi = int(input("Zadejte pozadovane mnozstvi: "))
    dostupne_mnozstvi = sklad[pozadovana_soucastka]

    if pozadovane_mnozstvi <= dostupne_mnozstvi:
        print("Poptavku lze uspokojit v plne vysi.")
        aktualni_mnozstvi = dostupne_mnozstvi - pozadovane_mnozstvi
        print (f"Aktualni mnozstvi soucastky {pozadovana_soucastka} je nyni {aktualni_mnozstvi} kusu.")
    else:
        print(f"Lze prodat pouze {dostupne_mnozstvi} kusu.")
        sklad.pop(pozadovana_soucastka)
        print("Zbyvajici soucastky na sklade:")
        for key in sklad.keys():
          print(key)
