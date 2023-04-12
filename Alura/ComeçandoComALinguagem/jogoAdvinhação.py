import random

print("-" * 20, "Jogo de advinhação!", "-" * 20)

chute = 0

level = int(input("Selecione o nível que deseja jogar:\n1- Fácil\n2- Intermediário\n3- Difícil\n4- Sair\n"))

while level > 4:
    level = int(
        input(
            "\nValor inválido, por favor selecione um dos seguintes níveis:\n1- Fácil\n2- Intermediário\n3- Difícil\n4- Sair\n"))

if level == 1:
    print("Você possui 3 chances para acertar um número de 1 até 10.")
    numeroSorteado = random.randrange(1, 11)
    chute = int(input("Qual número você deseja chutar primeiro?\n"))
elif level == 2:
    print("Você possui 3 chances para acertar um número de 1 até 20.")
    numeroSorteado = random.randrange(1, 21)
    chute = int(input("Qual número você deseja chutar primeiro?\n"))
elif level == 3:
    print("Você possui 3 chances para acertar um número de 1 até 30.")
    numeroSorteado = random.randrange(1, 31)
    chute = int(input("Qual número você deseja chutar primeiro?\n"))
else:
    print("Programa finalizado.")

i = 1
while chute != numeroSorteado and i < 3 and level < 4:
    chute = int(input("Qual número deseja chutar agora?\n"))
    i += 1

if chute != numeroSorteado and chute > 0:
    print("Não foi dessa vez. Tente novamente mais tarde.\n")
elif chute == numeroSorteado:
    print("Parabéns! Você acertou o número sorteado!\n")
