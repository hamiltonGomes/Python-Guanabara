valor = int(input("Digite o valor do produto:\n"))

valorDesconto = valor * 0.95
valorAumento = valor * 1.05

print("O valor à vista é R${}, já o valor parcelado é R${}.".format(valorDesconto, valorAumento))
