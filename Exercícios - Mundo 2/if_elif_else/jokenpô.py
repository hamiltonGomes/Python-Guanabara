import random

alternativas = ["Pedra", "Papel", "Tesoura"]
escolhaPC = random.choice(alternativas).lower()

print(20 * '=', "JOKENPÔ", 20 * '=')
escolhaPlayer = str(input("Digite \"Pedra\",\"Papel\" ou \"Tesoura\".\n"))
escolhaPlayer.lower()

print("Você escolheu {}! A máquina escolheu {}!".format(escolhaPlayer, escolhaPC))

if escolhaPC == escolhaPlayer:
    print("Empate!")
elif escolhaPlayer == "tesoura" and escolhaPC == "pedra":
    print("A máquina ganhou!")
elif escolhaPlayer == "tesoura" and escolhaPC == "papel":
    print("Você ganhou!")
elif escolhaPlayer == "pedra" and escolhaPC == "papel":
    print("A máquina ganhou!")
elif escolhaPlayer == "pedra" and escolhaPC == "tesoura":
    print("Você ganhou!")
elif escolhaPlayer == "papel" and escolhaPC == "tesoura":
    print("A máquina ganhou!")
elif escolhaPlayer == "papel" and escolhaPC == "pedra":
    print("Você ganhou!")
else:
    print("Dados inválidos.")
