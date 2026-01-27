intrestvoet = float(input("Jaarlijkse intrestvoet: "))
jaar = int(input("Aantal jaar: "))

totaal = 100 * (1+(intrestvoet/12))**(12*jaar)

print(round(totaal,2))