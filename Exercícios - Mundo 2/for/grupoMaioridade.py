# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year

maioresIdade = 0
menoresIdade = 0

for i in range(1, 8):
    anoNascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa (Exemplo: 2000): \n"))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        maioresIdade += 1
    else:
        menoresIdade += 1

print(f"Menores de idade: {menoresIdade}.\nMaiores de idade: {maioresIdade}.")