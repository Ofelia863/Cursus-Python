getal = int(input("Geef een getal: "))

getallen = []

for i in range(1,getal+1):
    getallen.append(i)

print(getallen)

print(getallen[0:3])

print(getallen[-4::])

print(getallen[1::2])

print(getallen[::-1])