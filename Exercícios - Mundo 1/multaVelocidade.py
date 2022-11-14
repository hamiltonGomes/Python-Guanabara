velocidade = int(input("Digite a velocidade do carro (km/h):\n"))

if velocidade > 80:
    velocidadeExcedida = velocidade - 80
    multa = velocidadeExcedida * 7
    print("Você foi multado em R$ {} por excesso de velocidade.".format(multa))
elif velocidade < 40:
    velocidadeAbaixo = 40 - velocidade
    multa = velocidadeAbaixo * 7
    print("Você foi multado em R$ {} por direção lenta.".format(multa))
else:
    print("Você está dentro do limite de velocidade. Siga em frente.")
