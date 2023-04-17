sequencia = []
numero = int(input("digite: "))
sequencia.append(numero)
while numero < 0:
    numero = int(input("valor inválido, digite um valor acima de 0: "))

while numero != 1:
    if numero == 0:
        break
    elif numero % 2 == 0:
        numero = numero / 2
    else:
        numero = 3 * numero + 1
    sequencia.append(int(numero))

print(f"({', '.join(map(str, sequencia))}", end=")")
