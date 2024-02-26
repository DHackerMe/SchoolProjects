# boh
from fractions import Fraction, math as m

def RisolviPrimoGrado():
    if b==0 and a==0:
        print("Equazione indeterminata.")
    else:
        if b==0: print("Equazione impossibile")
        else: print("x = "+(-c/b))

def CalcolaDelta():
    return b*b-4*a*c

def ScriviSoluzioni():
    delta = CalcolaDelta()
    if delta < 0:
        print("Non esistono soluzioni reali.")
    else:
        print("x1 = "+ str(x1 := Fraction(-b+m.sqrt(delta), (2*a))))
        print("x2 = "+ str(x2 := Fraction(-b-m.sqrt(delta), (2*a))))


print("Tre coefficienti: ", end="")
a = int(input())
b = int(input())
c = int(input())

if a != 0: ScriviSoluzioni()
else: RisolviPrimoGrado()