numeros_pares = []
numeros_impares = []

while True:
    numero = int(input("Digite um número: \n"))

    resposta = str(input("Deseja continuar? (S/N) \n"))
    while resposta not in "SsNn":
        resposta = str(input("Resposta inváldia. Deseja continuar? (S/N) \n"))

    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

    if resposta not in "Ss":
        break

print(f"\nOs números ímpares são: {', '.join(map(str, numeros_impares))}.\nNo total são {len(numeros_impares)}.")

print(f"\nOs números pares são: {', '.join(map(str, numeros_pares))}.\nNo total são {len(numeros_pares)}.")
