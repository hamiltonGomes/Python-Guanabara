lista1 = [int(x) for x in input("Digite a primeira lista com os elementos separados por espaço:\n").split()]
lista2 = [int(x) for x in input("Digite a segunda lista com os elementos separados por espaço:\n").split()]

par1 = 0
par2 = 0
menor = float('inf')

for x in lista1:
    for y in lista2:
        if menor > x - y >= 0:
            par1 = x
            par2 = y
            menor = x - y

print("Smallest difference: {}, pair: ({},{}).".format(menor, par1, par2))
