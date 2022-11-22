print("-" * 20, "MÁQUINA DE VENDAS DE BEBIDA", "-" * 20)

coke = 25
pepsi = 35
soda = 45
totalInserido = 0

valorInserido = int(input("Insira o valor desejado. Aceitamos moedas de 1, 5, 10 e 25 centavos.\nCaso deseje sair, digite 0."))


while valorInserido != 0:
    if valorInserido == 1 and valorInserido == 5 and valorInserido == 10 and valorInserido == 25:
        valorInserido = int(
            input("Caso ? Caso deseje sair, digite 0."))
        totalInserido = totalInserido + valorInserido
    else:
        valorInserido = int(input(
            "Valor inserido é inválido. Por favor, insira moedas de 1, 5, 10 e 25 centavos.\nCaso deseje sair, digite 0."))
