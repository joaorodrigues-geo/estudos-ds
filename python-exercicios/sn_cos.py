import math as m
angle = float(input("insira um grau: "))
cos = m.cos(m.radians(angle))
sn = m.sin(m.radians(angle))
tn= m.tan(m.radians(angle))
print("O seno equivale a: {:.2f}. \nO cosseno equivale a: {:.2f}. \na tangente equivale a: {:.2f}".format(sn, cos, tn ))