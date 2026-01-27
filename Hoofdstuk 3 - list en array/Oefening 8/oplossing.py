getallen = []
aantal_getallen = int(input("Hoeveel getallen wil je opgeven? "))
for keer in range(aantal_getallen):
    getal = int(input("Getal: "))
    getallen.append(getal)
for positie in range(len(getallen)):
    getallen[positie] = getallen[positie]*-1
for getal in getallen:
    print(getal)
'''cijfers = [4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 8, 9, 9.5, 10]

print(f'{cijfers[0]}|--|{cijfers[len(cijfers)//4]}--{cijfers[len(cijfers)//2]}--{cijfers[len(cijfers)//4*3]}|--|{cijfers[len(cijfers)-1]}')'''