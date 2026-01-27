# Maak een programma waarbij een gebruiker toetsresultaten kan ingeven. Er wordt herhaaldelijk gevraagd naar het behaalde resultaat ("Behaald: ") en op hoeveel de toets stond ("Op: "). De behaalde scores en de totalen van de toetsen worden in 2 aparte lijsten bijgehouden. Zolang de gebruiker niet "STOP" invult bij "Behaald: ", blijft dit doorgaan. Als de gebruiker een hogere behaalde score invult dan het totaal van de toets, moet deze opnieuw de behaalde score invullen (let op: de 'incorrecte' behaalde score van ervoor komt niet in de lijst). Ook als de gebruiker een totaal van 0 ingeeft, wordt deze iteratie als nietig beschouwd. Vervolgens toon je hoeveel toetsen de gebruiker heeft ingegeven en wat het gemiddelde was (gerond op 1 cijfer na de komma (zie round()). Per keer als de een toets werd ingegeven, toon je "Toets behaald/op werd toegevoegd.".
	Voorbeeld:
Behaald: 1
Op: 5
Toets 1.0/5.0 werd toegevoegd.
Behaald: 2
Op: 1
Behaald: 0
Op: 0
Behaald: 2
Op: 5
Toets 2.0/5.0 werd toegevoegd.
Behaald: STOP
Er werden 2 toetsen ingegeven.
Je hebt een gemiddelde van 30.0%.
