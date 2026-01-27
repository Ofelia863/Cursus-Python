gewicht = float(input("Hoeveel weegt uw pakket? "))

standaard_levering = 5 + (gewicht * 1.5)
express_levering = 12 + (gewicht * 0.8)

if standaard_levering < express_levering:
    print("Standaard levering")
if express_levering <= standaard_levering:
    print("Express levering")