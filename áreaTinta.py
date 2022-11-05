largura = int(input("Diga a largura da sua parede:\n"))
altura = int(input("Diga a altura da sua parede:\n"))

area = largura * altura
# 1L - 2m²
quantidadeTinta = area / 2

print(
    "A área da casa é {}m² e a quantidade de tinta necessária para sua pintura é de {}L.".format(area, quantidadeTinta))
