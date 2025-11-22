aantal = int(input("Aantal films: "))

films = []

for i in range(aantal):
    film = input("Titel film (van slecht naar goed): ")
    films.insert(0,film)

for i in range(len(films)):
    print(f'{i+1}. {films[i]}')
