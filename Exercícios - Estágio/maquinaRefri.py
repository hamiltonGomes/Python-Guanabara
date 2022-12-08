from datetime import datetime

dataHora = datetime.now()


class Hello:
    def hello(self):
        print("*" * 20, "Bem-vindo a máquina de refrigerantes!", "*" * 20)


ola = Hello()
ola.hello()


def vending_machine():
    global creditoTotal
    print("Aceitamos moedas de 0.01, 0.05, 0.10 ou 0.25 centavos.")
    list = [0.01, 0.05, 0.10, 0.25]
    creditoTotal = 0
    while True:
        moedaValor = float(input("\nAdicione o valor que deseja inserir: \n"))
        if moedaValor not in list:
            print("O valor inserido não é aceito, insira uma das seguintes moedas: 0.01, 0.05, 0.10 ou 0.25 centavos.")
        else:
            creditoTotal += moedaValor
        flag = str(input("Você deseja inserir outra moeda? [S/N] "))
        if flag in 'Nn':
            break
    produtos(creditoTotal)


def addMoedas():
    global creditoTotal
    list = [0.01, 0.05, 0.10, 0.25]
    flag = str(input("Você deseja inserir uma moeda? [S/N] "))
    if flag in 'Nn':
        print("\nCerto. Volte sempre.")
    else:
        moedaValor = float(input("Adicione o valor que deseja inserir: \n"))
        if moedaValor not in list:
            print("O valor inserido não é aceito, insira uma das seguintes moedas: 0.01, 0.05, 0.10 ou 0.25 centavos.")
        else:
            creditoTotal += moedaValor
            produtos(creditoTotal)


def produtos(creditoTotal):
    global creditoFinal
    creditoFinal = 0
    print("Você possui {:.2f} disponível.".format(creditoTotal))
    print("")
    print("1. Coca -> 25 centavos")
    print("2. Pepsi -> 35 centavos")
    print("3. Soda -> 45 centavos")
    print("4. Cancelar")
    print("")
    item = int(input("Insira o número do item desejado:  \n"))
    while 1 > item > 4:
        print("Este não é um valor válido.")
        item = int(input("Insira o número do item desejado: "))
    if item == 1:
        if creditoTotal < 0.25:
            print("\nVocê não possui saldo suficiente para comprar uma Coca.")
            addMoedas()
        else:
            creditoFinal = creditoTotal - 0.25
            print("\nVocê acaba de adquirir uma Coca, custando R$ 0.25.")
            print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
            confirmacao()
    elif item == 2:
        if creditoTotal < 0.35:
            print("\nVocê não possui saldo suficiente para comprar uma Pepsi.")
            addMoedas()
        else:
            creditoFinal = creditoTotal - 0.35
            print("\nVocê acaba de adquirir uma Pepsi, custando R$ 0.35.")
            print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
            confirmacao()
    elif item == 3:
        if creditoTotal < 0.45:
            print("\nVocê não possui saldo suficiente para comprar uma Soda.")
            addMoedas()
        else:
            creditoFinal = creditoTotal - 0.45
            print("\nVocê acaba de adquirir uma Soda, custando R$ 0.45.")
            print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
            confirmacao()
    elif item == 4:
        print("\nCerto! Processando o seu cancelamento em: " + dataHora.strftime('%d/%m/%Y às %H:%M.'))


def confirmacao():
    validacao = str(input("Você confirma o pedido? [S/N] "))
    if validacao in 'Nn':
        print(f"\nVocê será reembolsado ${creditoTotal}.")
        produtos(creditoTotal)
    else:
        print("\nVocê receberá {:.2f} como troco.".format(creditoFinal))
        print("Obrigado pela preferência, volte sempre!")


vending_machine()
