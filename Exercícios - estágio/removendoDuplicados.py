lista1 = input("Digite os valores da lista com espaço.").split()
lista2 = []

for x in lista1:
    if x not in lista2:
        lista2.append(x)

print(lista2)