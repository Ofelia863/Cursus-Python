getal = int(input("Getal: "))

origineel = getal

if getal < 0:
    getal = getal * -1

priemgetal = True

for deler in range(2,(getal//2)+1):
    if getal % deler == 0:
        priemgetal = False

if priemgetal:
    print(f'{origineel} is een priemgetal.')

if not priemgetal:
    print(f'{origineel} is geen priemgetal.')