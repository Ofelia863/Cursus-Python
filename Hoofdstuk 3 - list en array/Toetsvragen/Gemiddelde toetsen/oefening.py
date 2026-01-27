totaal = 0.0
aantal_toetsen = int(input("Hoeveel toetsen heb je? "))
for keer in range(aantal_toetsen):
    toets = float(input("Toets (op 10): "))
    totaal = totaal + toets
gemiddelde = totaal / aantal_toetsen
print(gemiddelde)