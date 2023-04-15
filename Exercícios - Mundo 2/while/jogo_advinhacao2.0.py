# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

numero_robo = random.randrange(0, 10)
print("----- Jogo da advinhação 2.0 -----")
palpite = int(input("Qual o número escolhido pelo computador?\n"))
total_palpites = 0

while palpite != numero_robo:
    total_palpites += 1
    if palpite < numero_robo:
        palpite = int(input("Mais... tente novamente! Digite o número: \n"))
    elif palpite > numero_robo:
        palpite = int(input("Menos... tente novamente! Digite o número: \n"))

print(f"\nParabéns! Você acertou!\nO número escolhido pelo computador era {numero_robo}.")
print(f"O seu total de palpites foi {total_palpites}!")
