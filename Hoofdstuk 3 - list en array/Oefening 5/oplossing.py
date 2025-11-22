ingredienten = []

for keer in range(1,4):
    ingr = input("Ingrediënt: ")
    ingredienten.append(ingr)
    #ingredienten.append(f'{keer}. {ingr}')

for teller in range(3):
    ingredienten[teller] = f'{teller+1}. {ingredienten[teller]}'

for ingr in ingredienten:
    print(ingr)


