from time import sleep


def soma(a, b):
    resultado = a + b
    return resultado


def subtracao(a, b):
    resultado = a - b
    return resultado


def multiplicacao(a, b):
    resultado = a * b
    return resultado


def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        resultado = a / b
        return f"A multiplicação entre {a} e {b} é igual a {resultado}."


def maior(a, b):
    if a > b:
        return a
    else:
        return b


def exibir_menu():
    sleep(2)
    print("-=-=- Menu -=-=-")
    print("[ 1 ] Somar")
    print("[ 2 ] Subtrair")
    print("[ 3 ] Multiplicar")
    print("[ 4 ] Dividir")
    print("[ 5 ] Maior")
    print("[ 6 ] Novos números")
    print("[ 7 ] Sair do programa")
    resposta = int(input("Digite uma das opções: \n"))
    while resposta not in range(1, 8):
        resposta = int(input("Digite uma opção válida: \n"))
    return resposta


print("--- Operações ---")

valor_a = float(input("Digite o primeiro valor: \n"))
valor_b = float(input("Digite o segundo valor: \n"))
resposta_usuario = exibir_menu()

while resposta_usuario != 7:
    if resposta_usuario == 1:
        print(f"A soma entre {valor_a} e {valor_b} é igual a {soma(valor_a, valor_b)}.\n")
    elif resposta_usuario == 2:
        print(f"A subtração entre {valor_a} e {valor_b} é igual a {subtracao(valor_a, valor_b)}.\n")
    elif resposta_usuario == 3:
        print(f"A multiplicação entre {valor_a} e {valor_b} é igual a {multiplicacao(valor_a, valor_b)}.\n")
    elif resposta_usuario == 4:
        print(divisao(valor_a, valor_b))
    elif resposta_usuario == 5:
        print(f"O maior valor entre {valor_a} e {valor_b} é igual a {maior(valor_a, valor_b)}.\n")
    elif resposta_usuario == 6:
        valor_a = float(input("Digite um novo primeiro valor: \n"))
        valor_b = float(input("Digite um novo segundo valor: \n"))
    resposta_usuario = exibir_menu()

print("\nObrigado por utilizar meu programa!")
