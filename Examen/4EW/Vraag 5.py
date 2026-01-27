films = []

for aantal in range(3):
    film = input("Film: ")
    films.append(film)

for positie in range(3):
    titel = films[positie]
    quote = input(f"Quote van {titel}: ")
    films[positie] = f'{titel}: "{quote}"'

print("Favoriete quotes: ")
for quote in films:
    print(quote)