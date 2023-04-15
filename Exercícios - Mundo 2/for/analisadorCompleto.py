# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

maisVelho = 0
nomeMaisVelho = ''
mulheresSub20 = 0
listaIdades = []

for i in range(1, 5):
    nome = str(input(f"Digite o nome da {i}ª pessoa: ")).strip()
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    sexo = str(input(f"Digite o sexo da {i}ª pessoa (M/F): ")).strip()
    listaIdades.append(idade)
    if i == 1 and sexo in "Mm":
        maisVelho = idade
        nomeMaisVelho = nome
    if sexo in "Mm" and idade > maisVelho:
        maisVelho = idade
        nomeMaisVelho = nome
    elif sexo in "Ff" and idade < 20:
        mulheresSub20 += 1

media = sum(listaIdades) / len(listaIdades)
print(f"\nA soma das idades é {media}.")
print(f"O homem mais velho se chama {nomeMaisVelho}.")
print(f"Ao todo são {mulheresSub20} mulheres com menos de 20 anos.")
