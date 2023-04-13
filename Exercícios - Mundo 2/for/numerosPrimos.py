# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

def obtendoNumero():
    """
    Solicita ao usuário um número inteiro positivo e retorna o valor digitado.
    """
    while True:
        numero = int(input("Digite o número que deseja desvendar: \n"))
        if numero > 0:
            return numero
        else:
            print("Digite um número inteiro positivo.\n")


def descobrirPrimalidade(numero):
    """
    Verifica se um número é primo e imprime uma mensagem informando o resultado.
    """
    numeroDivisoes = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            numeroDivisoes += 1

    if numeroDivisoes == 2:
        print(f"O número {numero} é primo.\n")
    else:
        print(f"O número {numero} não é primo.\n")


def selecionarOpcao():
    """
    Pergunta ao usuário se deseja continuar e retorna a resposta em minúsculas.
    """
    while True:
        opcao = input("Deseja continuar? (Sim/Não)\n").lower()
        if opcao in ["sim", "s"]:
            return "sim"
        elif opcao in ["nao", "não", "n"]:
            return "nao"
        else:
            print("Opção inválida. Tente inserir sim ou não.\n")


print("---Descobrindo números primos---")
while True:
    numero = obtendoNumero()
    descobrirPrimalidade(numero)
    opcao = selecionarOpcao()
    if opcao == "nao":
        print("Obrgigado.")
        break
