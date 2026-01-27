getal = int(input("Geef een grondgetal op: "))

for macht in range(1,11):
    nde_macht = getal ** macht
    print(f'{getal} tot de {macht}de = {nde_macht}')
    