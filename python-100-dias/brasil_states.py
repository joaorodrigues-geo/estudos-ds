#ex3 dictionary in a list with input
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = input("Digite a UF do estado: \n")
    estado['sigla'] = input("Digite a sigla do estado: \n")
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f"O estado {k} tem sigla {v}")
