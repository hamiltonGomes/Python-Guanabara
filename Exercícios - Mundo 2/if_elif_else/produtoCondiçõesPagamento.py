valor = float(input("Digite o valor do produto.\n"))
condicao = int(input(
    "Selecione a forma de pagamento:\n1- Dinheiro/cheque\n2- Cartão de crédito\n3- 2x no cartão de crédito (sem juros)\n4- 3x no cartão de crédito (com juros)\n"))

if condicao == 1:
    opcao1 = valor * 0.90  # dinheiro ou cheque
    print("O valor total fica R$ {:.2f}".format(opcao1))
elif condicao == 2:
    opcao2 = valor * 0.95  # cartão
    print("O valor total fica R$ {:.2f}".format(opcao2))
elif condicao == 3:
    opcao3 = valor  # 2x cartao
    print("O valor total fica R$ {:.2f}".format(opcao3))
elif condicao == 4:
    opcao4 = valor * 1.20  # 3x cartao
    print("O valor total fica R$ {:.2f}".format(opcao4))
else:
    print("Condição inválida.")
