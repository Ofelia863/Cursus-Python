aantal = int(input("Hoeveel toetsen heb je gemaakt? "))

punten = 0
totaal = 0

for keer in range(aantal):
    punten = punten + float(input("Behaald: "))
    totaal = totaal + float(input("Totaal: "))

percentage = punten / totaal

if percentage >= 0.5:
    print("Geslaagd")
if percentage < 0.5:
    print("Gebuisd")