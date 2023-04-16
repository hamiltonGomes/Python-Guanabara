soma = contador = 0
resposta = "S"
while resposta in "Ss":
    numero = int(input("Digite números inteiros: "))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta = str(input("Deseja continuar? (S/N)")).strip()[0]

media = soma / contador
print(media)
print(maior)
print(menor)
