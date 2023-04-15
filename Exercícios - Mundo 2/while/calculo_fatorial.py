numero = int(input("Digite o número que deseja saber o fatorial: \n"))
contador = numero
fatorial = 1
print(f"Calculando {numero}! = ", end='')

while contador > 0:
    print(f"{contador}", end='')
    print(" x " if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(f"{fatorial}.")
