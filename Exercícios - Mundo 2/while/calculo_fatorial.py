numero = int(input("Digite o número que deseja saber o fatorial: \n"))
contador = numero
fatorial = 1
resultado_fatorial = []

while contador > 0:
    fatorial *= contador
    resultado_fatorial.append(contador)
    contador -= 1

print(f"O fatorial de {numero}! = {' x '.join(map(str, resultado_fatorial))} = {fatorial}")
