appels = int(input("Appels: "))
druiven = int(input("Trossen druiven: "))

gewicht = (appels*0.150)+(druiven*0.600)
aantal_kisten = gewicht // 2.5
gewicht_zakje = (gewicht % 2.5)
#gewicht - (aantal_kisten * 2500)

print(f'Je hebt {aantal_kisten} kistjes nodig.')
print(f'Je hebt nog een zakje nodig voor {gewicht_zakje} kg fruit')
