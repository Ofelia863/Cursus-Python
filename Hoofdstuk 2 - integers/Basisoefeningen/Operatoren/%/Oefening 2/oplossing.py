pizzas = int(input("Aantal pizza's: "))
eters = int(input("Aantal eters: "))

rest = pizzas*8 % eters

print(f'{rest} stukken')