# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input("Digite o valor de KM percorridos:\n"))
dias = int(input("Informe a quantidade de dias que utilizou o carro:\n"))
valorTotal = (60*dias) + (0.15*km)

print("O valor total a ser pago é de R${:.2f}.".format(valorTotal))
