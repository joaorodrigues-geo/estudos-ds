import math as m
a = float(input("Insira o comprimento do primeiro cateto: "))
b = float(input("Insira o comprimento do segundo cateto: "))
#c = m.sqrt((a**2) + (b**2))
hp = m.hypot(a, b)
print("A hipotenusa equivale a: {:.2f}".format(hp))
