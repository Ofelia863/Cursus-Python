zomerse_dagen = 0
tropische_dagen = 0

for dag in range(7):
    temperatuur = float(input("Temperatuur: "))
    if temperatuur >= 25:
        zomerse_dagen = zomerse_dagen + 1
    if temperatuur >= 30:
        tropische_dagen = tropische_dagen + 1

if zomerse_dagen >= 5:
    if tropische_dagen >= 3:
        print("Hittegolf")