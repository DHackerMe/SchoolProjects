print("Studio del rettangolo")

base = input("Inserire la base: ")
altezza = input("Inserire l'altezza: ")

base = int(base)
altezza = int(altezza)

perimetro = (base + altezza) * 2
area = base * altezza

print("Il perimetro è " + str(perimetro))
print("L'area è " + str(area))