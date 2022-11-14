import math

catetoOposto = int(input("Valor do cateto oposto:\n"))
catetoAdjacente = int(input("Valor do cateto adjacente:\n"))
hipotenusa = math.sqrt(((catetoOposto ** 2) + (catetoAdjacente ** 2)))

print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))