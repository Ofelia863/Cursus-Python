buiten_marge = 0
standaard_inhoud = 33
marge = standaard_inhoud*0.05

for flesje in range(15):
    inhoud = float(input("Inhoud: "))
    if inhoud < standaard_inhoud - marge:
        buiten_marge = buiten_marge + 1
    if inhoud > standaard_inhoud + marge:
        buiten_marge = buiten_marge + 1

if buiten_marge > 3:
    print("Controleer de machine!")
