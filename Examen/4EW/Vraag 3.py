aantal = int(input("Hoeveel broers/zussen heb je: "))

namen = []
for keer in range(aantal):
    naam = input("Naam: ")
    namen.append(naam)

print(f"Je hebt een plaats gereserveerd voor {aantal} familieleden.")

for naam in namen:
    print(f'{naam} werd op de reservatielijst geplaatst.')
