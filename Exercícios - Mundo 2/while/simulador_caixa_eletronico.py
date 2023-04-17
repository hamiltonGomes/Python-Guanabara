print("=" * 30)
print("Bem vindo ao Caixa Eletrônico!")
print("=" * 30)

valor_desejado = int(input("Qual valor deseja sacar? \n"))
total = valor_desejado
cedulas_disponiveis = [50, 20, 10, 1]
total_cedulas = 0

if valor_desejado % min(cedulas_disponiveis) != 0:
    print("Valor inválido. O valor desejado não pode ser sacado com as cédulas disponíveis.")
else:
    for cedula in cedulas_disponiveis:
        while True:
            if total >= cedula:
                total -= cedula
                total_cedulas += 1
            else:
                if total_cedulas > 0:
                    print(f"Foram utilizadas {total_cedulas} de R$ {cedula}.")
                total_cedulas = 0
                break
