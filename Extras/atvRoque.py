def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def dividir(x, y):
    return x / y


print("Escolha uma operação:")
print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
choice = input("Resposta:\n")

while choice != '1' and choice != '2' and choice != '3' and choice != '4':
    choice = str(input("Valor inserido é inválido. Por favor, digite uma opção entre 1 ao 4."))
    if choice == "1" or choice == '2' or choice == '3' or choice == '4':
        break

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

if choice == '1':
    print(n1, "+", n2, "=", soma(n1, n2))
elif choice == '2':
    print(n1, "-", n2, "=", subtracao(n1, n2))
elif choice == '3':
    print(n1, "x", n2, "=", multiplicacao(n1, n2))
elif choice == '4':
    print(n1, "/", n2, "=", dividir(n1, n2))
