print("=========DESCOBRINDO TRIÂNGULOS=========")

ladoA = float(input("Digite o comprimento do primeiro lado:\n"))
ladoB = float(input("Digite o comprimento do segundo lado:\n"))
ladoC = float(input("Digite o comprimento do terceiro lado:\n"))

somaLadoAB = ladoA + ladoB
somaLadoBC = ladoB + ladoC
somaLadoCA = ladoC + ladoA

subLadoAB = ladoA - ladoB
if subLadoAB < 0:
    subLadoAB = subLadoAB * (-1)
subLadoBC = ladoB - ladoC
if subLadoBC < 0:
    subLadoBC = subLadoBC * (-1)
subLadoCA = ladoC - ladoA
if subLadoCA < 0:
    subLadoCA = subLadoCA * (-1)

if subLadoBC < ladoA < somaLadoBC or subLadoCA < ladoB < subLadoCA or subLadoAB < ladoC < somaLadoAB:
    if ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
        print("O triângulo existe e é equilátero!")
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("O triângulo existe e é escaleno!")
    else:
        print("O triângulo existe e é isósceles!")
else:
    print("O triângulo não existe!")

#  Condição de existência:
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
