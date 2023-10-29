num = input("Inserisci un numero: ")
num = int((num[::-1])[:1:])
while num > 1:
  num -= 2
if num == 0: print("Il numero è pari")
else: print("Il numero è dispari.")