getallen = []

'''getallen.append(int(input("Geef een getal: ")))
getallen.append(int(input("Geef een getal: ")))
getallen.append(int(input("Geef een getal: ")))'''


'''for getal in range(-1, -4, -1):
    getallen.append(getal)'''

'''for getal in range(1, 11, 3):
    getallen.append(getal)'''

for i in range(3):
    getallen.append(int(input("Geef een getal: ")))

som = 0
for getal in getallen:
    som = som + getal

print(som)
