numero = int(input("Insira um valor para desvendar a conjectura de Collatz (minímo 1).\n"))

while numero < 0:
    numero = int(input("Digite um número maior que 0 para descobrir a conjectura.\n"))

sequencia = [numero]

while numero > 1:
    if numero % 2 == 0:
        numero = numero / 2

    elif numero % 2 != 0:
        numero = 3 * numero + 1

    sequencia.append(int(numero))

if numero == 0:
    print("Programa finalizado.")
else:
    print("Sequence = {}".format(sequencia).replace("[", "(").replace("]", ")"))

