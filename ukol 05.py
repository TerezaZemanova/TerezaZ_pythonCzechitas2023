teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
prumerne_teploty = []
ranní_teploty = []
nocni_teploty = []
poledni_a_nocni = []

for den in teploty:
    denni_prumer = round(sum(den) / len(den), 2)
    prumerne_teploty.append(denni_prumer)
    ranní_teploty.append(den[0])
    nocni_teploty.append(den[3])
    poledni_a_nocni.append(den[1:3])

print("Průměrné teploty:", prumerne_teploty)
print("Ranní teploty:", ranní_teploty)
print("Noční teploty:", nocni_teploty)
print("Polední a noční teploty:", poledni_a_nocni)
