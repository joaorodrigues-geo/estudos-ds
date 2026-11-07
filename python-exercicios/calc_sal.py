sal = float(input("Digite o valor do salario: "))
#nsal = sal * 1.15
nsal = sal + (sal * 15/100)
print("o valor do seu salario apos o aumento de 15% é de: {}€".format(nsal))