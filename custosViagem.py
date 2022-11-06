distancia = float(input("Qual a distância da sua viagem?\n"))

if distancia > 200:
    value1 = distancia * 0.5
    print("O preço da passagem é R$ {:.2f}.".format(value1))
else:
    value2 = distancia * 0.45
    print("O preço da passagem é de R$ {:.2f}.".format(value2))

