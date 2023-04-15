# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input("Digite o sexo: ")).strip()[0]
    while sexo not in "MmFf" or sexo == '':
        sexo = str(input("Valor informado inválido, por favor, digite M ou F: ")).strip()[0]
    if sexo in "Mm":
        sexo = "masculino"
    else:
        sexo = "feminino"
    break

print(f"Seu sexo é: {sexo}.")
