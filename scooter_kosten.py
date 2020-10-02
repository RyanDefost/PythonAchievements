# schrijf Functie 'bereken_maandkosten()' accepteerd alleen km_per_maand
# rekent het uit met ^ en return doet
# input() vraag
# zorg dat het zeker een int is
# Roep 'berekening_maandkosten()' op en doe print()

verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

print("Hoe veel km rijd je per maand? ")
km_per_maand = input(": ")

def MaandKosten(waardeA, waardeB, waardeC, waardeD):
    return ((waardeA * waardeB * waardeC) + waardeD)

kosten = MaandKosten(float(km_per_maand), liter_per_kilometer, benzine_kosten_per_liter, float(verzekering_per_maand))
print("je maandelijkse kosten zijn dan:", kosten, "Euro")

print("\n------------------------------------------------------")
print(verzekering_per_maand)
print(benzine_kosten_per_liter)
print(liter_per_kilometer)
print(km_per_maand)


