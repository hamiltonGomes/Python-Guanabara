def vending_machine():
    global creditoTotal
    print("Bem-vindo a máquina de vendas!")
    print("Aceitamos moedas de 0.01, 0.05, 0.10 ou 0.25 centavos.")
    list = [0.01, 0.05, 0.10, 0.25]
    creditoTotal = 0
    while True:
        moedaValor = float(input("Adicione o valor que deseja inserir: \n"))
        if moedaValor not in list:
            print("O valor inserido não é aceito, insira uma das seguintes moedas: 0.01, 0.05, 0.10 ou 0.25 centavos.")
            print("Você receberá um reembolso.")
        else:
            creditoTotal += moedaValor
        flag = str(input("Você deseja inserir outra moeda? [S/N] "))
        if flag in 'Nn':
            break
    produtos(creditoTotal)


def produtos(creditoTotal):
    global creditoFinal
    creditoFinal = 0
    print("Você possui {:.2f} disponível.".format(creditoTotal))
    print("")
    print("1. Coke -> 25 centavos")
    print("2. Pepsi -> 35 centavos")
    print("3. Soda -> 45 centavos")
    print("")
    item = int(input("Insira o número do item desejado:  \n"))
    while 1 > item > 3:
        print("Este não é um valor válido.")
        item = int(input("Insira o número do item desejado: "))
    if item == 1:
        creditoFinal = creditoTotal - 0.25
        print("Você acaba de adquirir uma Coke, custando R$ 0.25.")
        print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
    elif item == 2:
        creditoFinal = creditoTotal - 0.35
        print("Você acaba de adquirir uma Pepsi, custando R$ 0.35.")
        print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
    elif item == 3:
        creditoFinal = creditoTotal - 0.45
        print("Você acaba de adquirir uma Soda, custando R$ 0.45.")
        print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
    confirmacao()


def confirmacao():
    validacao = str(input("Você confirma o pedido? [S/N] "))
    if validacao in 'Nn':
        print(f"Você será reembolsado ${creditoTotal}.")
        produtos(creditoTotal)
    else:
        print("Você receberá {:.2f} como troco.".format(creditoFinal))
        print("Pode retirar o produto.")


vending_machine()
