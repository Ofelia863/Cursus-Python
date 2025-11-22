getal = int(input("Geef een getal in: "))

tafels_van_10 = []

for factor in range(1,11):
    tafels_van_10.append(factor*getal)

for tafel in tafels_van_10:
    print(tafel)

for positie in range(len(tafels_van_10)):
    tafels_van_10[positie] = tafels_van_10[positie]**2

print(tafels_van_10)