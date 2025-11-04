''' Berekeningen

Maak een programma dat aan de gebruiker een aantal pizza's vraag die hij wenst te bestellen 
("Aantal pizza's: "). 
Een pizza kost € 14,50 euro, en je hebt een speciale deal: 4 + 1 gratis! 
Laat de gebruiker het aantal pizza's ingeven en bereken de totale prijs. 
Toon deze vervolgens op het scherm ("Prijs: ... euro")

Bv. 
Aantal pizza's: 5
Prijs: 58.00 euro

Aantal pizza's: 6
Prijs: 72.50 euro'''

aantal = int(input("Aantal pizza's: "))

prijs = 14.5

pizzas_per_deal = 4 + 1

prijs_per_deal = 4 * prijs

aantal_keer_deal = aantal // pizzas_per_deal

aantal_pizzas_buiten_deal = aantal % pizzas_per_deal

# of aantal_pizzas_buiten_deal = aantal - (aantal_keer_deal * pizzas_per_deal)

totaal = (aantal_keer_deal * prijs_per_deal) + (aantal_pizzas_buiten_deal * prijs)

print(f'Prijs: {totaal} euro')
