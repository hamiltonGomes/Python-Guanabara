lista = [0]

for i in range(0, 6):
    valorLista = int(input("Digite 1 número:\n"))
    if valorLista % 2 == 0:
        lista.append(valorLista)

somaLista = sum(lista)

print(f"O valor dos números pares é igual a {somaLista}.")
