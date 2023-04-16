numero = int(input("Insira um valor para desvendar a progressão (minímo 1).\n"))

while numero < 0:
    numero = int(input("Digite um número maior que 0 para descobrir a progressão.\n"))

print(numero)
sequencia = [numero]

while numero > 1:
    if numero % 2 == 0:
        numero /= 2

    elif numero % 2 != 0:
        numero = 3 * numero + 1

    sequencia.append(int(numero))

print(sequencia)
