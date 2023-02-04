print("Determine o intervalo:")
inicio = int(input("O intervalo inicia-se em: "))
final = int(input("O intervalo se encerra em: "))

for i in range(inicio, final):
    if i % 2 == 0:
        print(i)